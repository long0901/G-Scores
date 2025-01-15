import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from scores.models import Student, Score
from django.db.models import Q
from concurrent.futures import ThreadPoolExecutor
import numpy as np

class Command(BaseCommand):
    help = 'Import scores from CSV file'

    def handle(self, *args, **options):
        try:
            # Đọc file CSV với chunk size để xử lý file lớn
            csv_file = 'dataset/diem_thi_thpt_2024.csv'
            self.stdout.write(f'Reading CSV file: {csv_file}')
            
            # Sử dụng chunk_size để đọc file lớn
            chunk_size = 10000
            
            # Mapping tên cột
            subject_mapping = {
                'toan': 'Mathematics',
                'ngu_van': 'Literature',
                'ngoai_ngu': 'Foreign Language',
                'vat_li': 'Physics',
                'hoa_hoc': 'Chemistry',
                'sinh_hoc': 'Biology',
                'lich_su': 'History',
                'dia_li': 'Geography',
                'gdcd': 'Civic Education'
            }

            students_created = 0
            scores_created = 0

            # Đọc và xử lý từng chunk
            for chunk_number, df_chunk in enumerate(pd.read_csv(csv_file, dtype={'sbd': str}, chunksize=chunk_size)):
                self.stdout.write(f'Processing chunk {chunk_number + 1}')
                
                # Chuẩn bị dữ liệu cho bulk create
                student_data = []
                score_data = []
                existing_students = set(Student.objects.values_list('registration_number', flat=True))

                with transaction.atomic():
                    # Tạo danh sách học sinh mới
                    new_students = []
                    for _, row in df_chunk.iterrows():
                        # Đảm bảo số báo danh luôn có 8 chữ số
                        reg_number = str(row['sbd']).strip().zfill(8)
                        if reg_number not in existing_students:
                            new_students.append(Student(registration_number=reg_number))
                            existing_students.add(reg_number)
                    
                    # Bulk create students
                    if new_students:
                        Student.objects.bulk_create(new_students, batch_size=1000)
                        students_created += len(new_students)

                    # Lấy mapping student_id
                    student_id_map = dict(Student.objects.filter(
                        registration_number__in=df_chunk['sbd'].astype(str).str.strip()
                    ).values_list('registration_number', 'id'))

                    # Chuẩn bị dữ liệu điểm số
                    scores_to_create = []
                    for _, row in df_chunk.iterrows():
                        student_id = student_id_map[str(row['sbd']).strip()]
                        
                        for csv_subject, display_name in subject_mapping.items():
                            if pd.notna(row[csv_subject]):
                                try:
                                    score_value = float(row[csv_subject])
                                    scores_to_create.append(
                                        Score(
                                            student_id=student_id,
                                            subject=display_name,
                                            score=score_value
                                        )
                                    )
                                except ValueError:
                                    self.stdout.write(
                                        self.style.WARNING(
                                            f'Invalid score value for student {row["sbd"]}, '
                                            f'subject {csv_subject}: {row[csv_subject]}'
                                        )
                                    )

                    # Bulk create scores
                    if scores_to_create:
                        Score.objects.bulk_create(
                            scores_to_create,
                            batch_size=1000,
                            ignore_conflicts=True
                        )
                        scores_created += len(scores_to_create)

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Processed chunk {chunk_number + 1}: '
                        f'{len(new_students)} students, {len(scores_to_create)} scores'
                    )
                )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully imported {students_created} students and {scores_created} scores'
                )
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error importing data: {str(e)}')
            )
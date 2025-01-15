from django.shortcuts import render
from django.db.models import Count, Case, When, F, Q, Avg, Value, IntegerField, Sum, DecimalField
from django.db.models.functions import Coalesce
from .models import Student, Score

def home_view(request):
    return render(request, 'home.html')

def score_check_view(request):
    result = None
    reg_number = ''
    if 'registration_number' in request.GET:
        reg_number = request.GET['registration_number'].strip()
        student = Student.objects.filter(registration_number=reg_number).first()
        if student:
            result = Score.objects.filter(student=student)
    
    return render(request, 'score_check.html', {
        'result': result,
        'registration_number': reg_number
    })

def statistics_view(request):
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Literature', 
                'Foreign Language', 'Biology', 'History', 'Geography', 'Civic Education']
    
    stats_data = []
    for subject_name in subjects:
        level_stats = Score.objects.filter(subject=subject_name).aggregate(
            excellent=Count(Case(
                When(score__gte=8, then=1),
                output_field=IntegerField(),
            )),
            good=Count(Case(
                When(score__lt=8, score__gte=6, then=1),
                output_field=IntegerField(),
            )),
            average=Count(Case(
                When(score__lt=6, score__gte=4, then=1),
                output_field=IntegerField(),
            )),
            poor=Count(Case(
                When(score__lt=4, then=1),
                output_field=IntegerField(),
            ))
        )
        
        stats_data.append({
            'subject': subject_name,
            'stats': level_stats,
            'total': sum(level_stats.values())
        })
    
    return render(request, 'statistics.html', {
        'stats_data': stats_data,
        'chart_labels': [item['subject'] for item in stats_data],
        'chart_data': {
            'excellent': [item['stats']['excellent'] for item in stats_data],
            'good': [item['stats']['good'] for item in stats_data],
            'average': [item['stats']['average'] for item in stats_data],
            'poor': [item['stats']['poor'] for item in stats_data]
        }
    })

def top_students_view(request):
    # Lấy top 10 học sinh khối A (Toán, Lý, Hóa)
    top_students = (
        Student.objects.annotate(
            mathematics_score=Coalesce(
                Sum('scores__score', filter=Q(scores__subject='Mathematics')),
                0,
                output_field=DecimalField(max_digits=4, decimal_places=2)
            ),
            physics_score=Coalesce(
                Sum('scores__score', filter=Q(scores__subject='Physics')),
                0,
                output_field=DecimalField(max_digits=4, decimal_places=2)
            ),
            chemistry_score=Coalesce(
                Sum('scores__score', filter=Q(scores__subject='Chemistry')),
                0,
                output_field=DecimalField(max_digits=4, decimal_places=2)
            ),
        )
        .annotate(
            total_score=(
                F('mathematics_score') + 
                F('physics_score') + 
                F('chemistry_score')
            )
        )
        .filter(
            mathematics_score__gt=0,
            physics_score__gt=0,
            chemistry_score__gt=0
        )
        .order_by('-total_score')[:10]
        .values(
            'registration_number',
            'mathematics_score',
            'physics_score', 
            'chemistry_score',
            'total_score'
        )
    )

    return render(request, 'top_students.html', {'top_students': top_students})
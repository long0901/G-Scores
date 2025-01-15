from django.db import models

class Student(models.Model):
    registration_number = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.registration_number

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scores')
    subject = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=4, decimal_places=2)
    
    class Meta:
        unique_together = ['student', 'subject']
    
    def __str__(self):
        return f"{self.student.registration_number} - {self.subject}: {self.score}"
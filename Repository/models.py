from django.db import models

# Create your models here.
"""
Scheme : QuestionDb
Fields : title,language,difficulty_level,notes,sample_input,sample_output,topic,published_date,is_active
"""
class QuestionDb(models.Model):
    title=models.CharField(max_length=200)

    LANGUAGE_CHOICES=(
        ('Python','Python'),
        ('Java','Java'),
        ('C++','C++'),
        ('JavaScript','JavaScript'),
    )
    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default="Python")

    DIFFICULTY_CHOICES=(
        ("easy","easy"),
        ("medium","medium"),
        ("hard","hard")
    )
    difficulty_level=models.CharField(max_length=100,choices=DIFFICULTY_CHOICES,default="easy")

    
    topic=models.CharField(max_length=200)

    notes=models.TextField()

    published_date=models.DateField(auto_now_add=True)   

    is_active=models.BooleanField(default=True)   

    sample_input=models.TextField()

    sample_output=models.TextField()
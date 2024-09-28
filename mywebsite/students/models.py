from typing import Iterable
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_date']
        

class Teacher(models.Model):
    GENDER_CHOICES = (
        ('N', 'Not Specified'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='N')
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        print('Teacher saved')
        super(Teacher, self).save()
        
    def update_full_name(self):
        self.full_name = 'School Teacher'
        self.save()
    
    def __str__(self):
        return self.full_name
            
    class Meta:
        db_table = 'teacher'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'student'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        
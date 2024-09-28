from django.shortcuts import render, get_object_or_404
from .models import Student, Category, Teacher
from django.db.models import Q

# Create your views here.

def index(request):
    # students = get_object_or_404(Student, first_name="Metin")
    students = Student.objects.filter(first_name="Metin")    
    students = Student.objects.filter(first_name__isnull=True)    
    students = Student.objects.filter(first_name__contains="e")    
    students = Student.objects.filter(first_name__startswith="M")    
    students = Student.objects.filter(first_name__icontains="e", first_name__endswith="r")    
    students = Student.objects.filter(Q(first_name__icontains="e") & Q(first_name__endswith="r"))
    students = Student.objects.filter(Q(first_name__icontains="e") | Q(first_name__endswith="r"))
    students = Student.objects.exclude(first_name="Metin")
    students = Student.objects.all().order_by('first_name')
    student = Student.objects.filter(first_name='Ebubekir').exists()
    student = Student.objects.filter(first_name='Metin').count()
    # print(student)
    # print(students)
    
    # teacher = Teacher.objects.create(
    #     full_name = 'Teacher 4',
    #     gender = 'M',
    #     age = 30
    # )
    teacher = Teacher.objects.get(full_name='New Teacher')
    teacher.full_name = 'New Teacher'
    teacher.age = 26
    teacher.save()
    # print(teacher)
    
    first_student = Student.objects.first()
    last_student = Student.objects.last()
    # print(first_student)
    # print(last_student)
    
    student = Student.objects.filter(teacher__full_name='Teacher 2')
    student = Student.objects.filter(teacher__full_name__startswith='T')
    student = Student.objects.filter(teacher__full_name__in=['Teacher 1', 'Teacher 2'])
    print(student)
    
    categories = Category.objects.filter(name='Programmer')
    student = Student.objects.filter(
        category__in = categories
    )
    print(student)
    
    teacher = Teacher.objects.first()
    teacher.update_full_name()
    
    
    return render(request, 'students/index.html')

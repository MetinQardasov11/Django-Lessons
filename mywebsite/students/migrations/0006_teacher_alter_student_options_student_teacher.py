# Generated by Django 5.1.1 on 2024-09-24 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_remove_student_category_student_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.teacher'),
        ),
    ]

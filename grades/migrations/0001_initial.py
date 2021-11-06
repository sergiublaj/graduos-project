# Generated by Django 3.2.9 on 2021-11-06 19:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_person_photo'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor_Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('file_uploaded', models.FileField(upload_to='')),
                ('percentage', models.IntegerField(default=100)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.course')),
                ('professor_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, max_digits=4)),
                ('submitted', models.BooleanField(default=False)),
                ('file_uploaded', models.FileField(upload_to='')),
                ('assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.professor_assignment')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, max_digits=4)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.student')),
            ],
        ),
    ]

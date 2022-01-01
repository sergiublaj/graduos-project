# Generated by Django 3.2.9 on 2021-12-29 15:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor_Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('uploaded_date', models.DateTimeField(default=datetime.datetime.now)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now)),
                ('task_file', models.FileField(upload_to='assignments/%Y/')),
                ('percentage', models.IntegerField(default=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.course')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('submitted', models.BooleanField(default=False)),
                ('task_file', models.FileField(null=True, upload_to='assignments/%Y/')),
                ('uploaded_date', models.DateTimeField(default=datetime.datetime.now)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.professor_assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=2, max_digits=4)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.student')),
            ],
        ),
    ]

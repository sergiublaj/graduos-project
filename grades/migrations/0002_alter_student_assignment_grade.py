# Generated by Django 3.2.9 on 2021-12-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_assignment',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]

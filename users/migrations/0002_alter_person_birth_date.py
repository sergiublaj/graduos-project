# Generated by Django 3.2.9 on 2021-12-25 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.date(2003, 12, 30)),
        ),
    ]

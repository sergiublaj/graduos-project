# Generated by Django 3.2.9 on 2021-12-26 17:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_content', models.CharField(max_length=5000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(blank=True, upload_to='images/posts/%Y/%M')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_content', models.CharField(max_length=5000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(default='', upload_to='images/posts/%Y/%M')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='forum.post')),
            ],
        ),
    ]

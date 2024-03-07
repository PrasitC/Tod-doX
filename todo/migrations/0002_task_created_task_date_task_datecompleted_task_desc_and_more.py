# Generated by Django 5.0.3 on 2024-03-06 10:25

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='desc',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='task',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
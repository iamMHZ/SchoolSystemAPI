# Generated by Django 3.2 on 2021-06-05 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 3.2 on 2021-05-19 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='user',
            new_name='teacher',
        ),
    ]
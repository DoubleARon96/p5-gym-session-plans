# Generated by Django 5.0.6 on 2024-07-09 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0006_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
    ]
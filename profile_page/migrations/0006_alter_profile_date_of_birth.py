# Generated by Django 5.0.6 on 2024-07-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0005_alter_profile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
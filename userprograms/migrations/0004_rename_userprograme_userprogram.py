# Generated by Django 5.0.6 on 2024-08-09 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprograms', '0003_alter_userprograme_exercise_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserPrograme',
            new_name='UserProgram',
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptsessions', '0004_alter_ptsessions_program_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ptsessions',
            name='price_in_pounds',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
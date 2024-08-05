# Generated by Django 5.0.6 on 2024-08-05 20:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptsessions', '0011_remove_ptsessions_client_ptsessions_client'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptsessions',
            name='client',
            field=models.ManyToManyField(blank=True, related_name='client_sessions', to=settings.AUTH_USER_MODEL),
        ),
    ]

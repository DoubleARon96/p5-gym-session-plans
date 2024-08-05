# Generated by Django 5.0.6 on 2024-08-05 20:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptsessions', '0008_ptsessions_item_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptsessions',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_sessions', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptsessions', '0007_remove_ptsessions_price_in_pounds_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ptsessions',
            name='item_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
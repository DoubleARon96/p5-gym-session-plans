# Generated by Django 3.2.25 on 2024-06-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=30)),
                ('content', models.TextField(max_length=2000)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

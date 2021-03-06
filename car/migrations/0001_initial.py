# Generated by Django 3.2.5 on 2021-08-11 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('price', models.FloatField()),
                ('transmission', models.CharField(max_length=400)),
                ('engine', models.CharField(max_length=400)),
                ('drivetrain', models.CharField(max_length=400)),
                ('weight', models.FloatField()),
                ('needs_fixin', models.CharField(max_length=4000)),
                ('updated', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]

# Generated by Django 5.0 on 2024-01-04 12:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=250)),
                ('explanation', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=250)),
                ('country', models.CharField(default='korea', max_length=50)),
                ('city', models.CharField(default='Seoul', max_length=80)),
                ('price', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=250)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('descriptions', models.TextField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('perks', models.ManyToManyField(to='experiences.perk')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

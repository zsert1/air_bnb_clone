# Generated by Django 5.0 on 2023-12-26 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_rename_price_house_price_per_night'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='pets_allow',
            field=models.BooleanField(default=True),
        ),
    ]

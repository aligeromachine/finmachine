# Generated by Django 5.2 on 2025-07-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0007_cards_enable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cards',
            name='enable',
        ),
        migrations.AddField(
            model_name='cards',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]

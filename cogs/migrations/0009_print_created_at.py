# Generated by Django 4.2.1 on 2023-08-08 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cogs', '0008_changeover_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='print',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

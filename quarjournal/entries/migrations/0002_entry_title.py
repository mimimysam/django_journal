# Generated by Django 2.2.16 on 2020-10-11 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.TextField(default='Untitled'),
        ),
    ]

# Generated by Django 5.1.7 on 2025-03-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]

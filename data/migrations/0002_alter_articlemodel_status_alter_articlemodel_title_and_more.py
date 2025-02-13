# Generated by Django 5.1.6 on 2025-02-12 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='knowledgemodel',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='knowledgemodel',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

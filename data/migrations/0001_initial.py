# Generated by Django 5.1.6 on 2025-02-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(default='publish', max_length=10)),
                ('summary', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='KnowledgeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(default='publish', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=255)),
                ('articles', models.ManyToManyField(blank=True, to='data.articlemodel')),
            ],
            options={
                'db_table': 'knowledge',
            },
        ),
    ]

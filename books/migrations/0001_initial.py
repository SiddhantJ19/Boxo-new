# Generated by Django 2.2 on 2019-05-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(blank=True, max_length=150, null=True)),
                ('genre', models.CharField(max_length=150, null=True)),
                ('published', models.CharField(max_length=150, null=True)),
                ('poster', models.URLField(null=True)),
                ('author', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]

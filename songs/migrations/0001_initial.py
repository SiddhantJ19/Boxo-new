# Generated by Django 2.2 on 2019-05-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(blank=True, max_length=150, null=True)),
                ('type', models.CharField(max_length=150, null=True)),
                ('artist_album', models.CharField(max_length=150, null=True)),
                ('released', models.CharField(max_length=150, null=True)),
                ('rating', models.CharField(max_length=150, null=True)),
                ('poster', models.URLField(null=True)),
                ('runtime', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]

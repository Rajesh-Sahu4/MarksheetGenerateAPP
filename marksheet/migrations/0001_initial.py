# Generated by Django 4.2.11 on 2024-06-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='markupdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('sub1', models.CharField(max_length=25)),
                ('mark1', models.IntegerField()),
                ('sub2', models.CharField(max_length=25)),
                ('mark2', models.IntegerField()),
                ('sub3', models.CharField(max_length=25)),
                ('mark3', models.IntegerField()),
                ('sub4', models.CharField(max_length=25)),
                ('mark4', models.IntegerField()),
                ('sub5', models.CharField(max_length=25)),
                ('mark5', models.IntegerField()),
                ('sub6', models.CharField(max_length=25)),
                ('mark6', models.IntegerField()),
            ],
        ),
    ]

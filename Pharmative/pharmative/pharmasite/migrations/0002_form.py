# Generated by Django 3.1.7 on 2021-04-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmasite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_fname', models.CharField(max_length=20)),
                ('c_lname', models.CharField(max_length=20)),
                ('c_email', models.CharField(max_length=25)),
                ('c_subject', models.CharField(max_length=30)),
                ('c_message', models.CharField(max_length=300)),
            ],
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-15 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

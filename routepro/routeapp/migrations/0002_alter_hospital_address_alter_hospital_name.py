# Generated by Django 4.1.7 on 2023-02-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 5.0 on 2023-12-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_studentregister_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='mobile',
            field=models.CharField(max_length=25),
        ),
    ]

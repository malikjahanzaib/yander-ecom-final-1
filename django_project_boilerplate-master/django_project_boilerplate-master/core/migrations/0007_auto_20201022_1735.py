# Generated by Django 3.0.8 on 2020-10-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201016_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 3.1.2 on 2021-02-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RTH', '0002_auto_20210201_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktable',
            name='num_of_person',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 3.1.6 on 2021-04-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0011_auto_20210423_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='product',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

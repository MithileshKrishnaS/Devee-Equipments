# Generated by Django 3.1.6 on 2021-04-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0005_auto_20210329_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]

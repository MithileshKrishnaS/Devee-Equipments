# Generated by Django 3.1.6 on 2021-03-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0002_auto_20210323_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
    ]

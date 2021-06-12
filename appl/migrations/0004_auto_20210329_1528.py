# Generated by Django 3.1.6 on 2021-03-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0003_auto_20210326_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='frequency',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='phase',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='usage',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='voltage',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
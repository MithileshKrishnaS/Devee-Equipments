# Generated by Django 3.1.6 on 2021-04-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appl', '0012_auto_20210425_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

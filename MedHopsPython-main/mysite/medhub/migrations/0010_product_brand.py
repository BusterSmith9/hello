# Generated by Django 3.1.7 on 2021-03-14 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medhub', '0009_auto_20210313_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=100),
        ),
    ]
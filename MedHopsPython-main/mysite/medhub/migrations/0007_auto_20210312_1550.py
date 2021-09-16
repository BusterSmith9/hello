# Generated by Django 3.1.7 on 2021-03-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medhub', '0006_auto_20210312_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='mesg_id',
            new_name='msg_id',
        ),
    ]
# Generated by Django 2.0.6 on 2018-06-14 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0013_auto_20180614_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='txt',
        ),
    ]
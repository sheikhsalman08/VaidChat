# Generated by Django 2.0.6 on 2018-06-14 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0012_auto_20180614_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msgs',
            name='ChatRoom',
        ),
        migrations.DeleteModel(
            name='Msgs',
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-14 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0002_auto_20180614_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg',
            name='ChatRoom',
        ),
        migrations.AddField(
            model_name='msg',
            name='ChatRoom2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Chat.Test'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-14 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Chat', '0010_auto_20180614_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.CharField(blank=True, max_length=10000, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('ChatRoom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Chat.ChatRoom')),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='msg',
            name='ChatRoom',
        ),
        migrations.RemoveField(
            model_name='msg',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='msg',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Msg',
        ),
    ]

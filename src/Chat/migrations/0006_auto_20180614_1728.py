# Generated by Django 2.0.6 on 2018-06-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0005_auto_20180614_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='tst',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tst',
            name='txt',
            field=models.CharField(default='', max_length=10000),
            preserve_default=False,
        ),
    ]

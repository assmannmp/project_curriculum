# Generated by Django 2.1.7 on 2019-03-05 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_auto_20190304_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='user',
        ),
    ]

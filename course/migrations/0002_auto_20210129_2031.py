# Generated by Django 2.2 on 2021-01-29 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='massage_request',
            new_name='post_data',
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-21 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats_server', '0002_remove_stats_username_stats_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stats',
            old_name='user',
            new_name='username',
        ),
    ]
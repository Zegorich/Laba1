# Generated by Django 5.0.3 on 2024-05-18 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_rename_registration_code_flag_user_flag_registration_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='flag_registration_code',
            new_name='registration_code_flag',
        ),
    ]

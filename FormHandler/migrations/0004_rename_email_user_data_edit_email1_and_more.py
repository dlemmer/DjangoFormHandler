# Generated by Django 4.2.7 on 2023-11-26 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormHandler', '0003_user_data_edit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_data_edit',
            old_name='email',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='user_data_edit',
            old_name='name',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='user_data_edit',
            old_name='reg_data',
            new_name='reg_data1',
        ),
        migrations.RenameField(
            model_name='user_data_edit',
            old_name='reg_time',
            new_name='reg_time1',
        ),
        migrations.RenameField(
            model_name='user_data_edit',
            old_name='surname',
            new_name='surname1',
        ),
        migrations.RemoveField(
            model_name='user_data_edit',
            name='agreement_check',
        ),
    ]
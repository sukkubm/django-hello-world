# Generated by Django 3.0.4 on 2020-03-17 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('say_hello', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Message',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='name',
            new_name='text',
        ),
    ]

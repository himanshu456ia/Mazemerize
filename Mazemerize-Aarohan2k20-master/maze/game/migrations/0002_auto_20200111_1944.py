# Generated by Django 3.0.1 on 2020-01-11 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('-moves',)},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='points',
            new_name='moves',
        ),
    ]

# Generated by Django 2.0.3 on 2018-06-20 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greinar', '0015_greinar_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greinar',
            name='image',
        ),
    ]

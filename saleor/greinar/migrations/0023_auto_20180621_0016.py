# Generated by Django 2.0.3 on 2018-06-21 00:16

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('greinar', '0022_auto_20180621_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greinar',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='greinar_myndir'),
        ),
    ]

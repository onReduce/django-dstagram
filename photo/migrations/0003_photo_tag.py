# Generated by Django 2.1.1 on 2018-09-10 01:54

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_photo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='tag',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
    ]

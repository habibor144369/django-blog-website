# Generated by Django 3.1.5 on 2021-01-21 07:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0017_auto_20210120_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_comment',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

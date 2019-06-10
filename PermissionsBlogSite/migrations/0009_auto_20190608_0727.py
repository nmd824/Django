# Generated by Django 2.2.1 on 2019-06-08 07:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PermissionsBlogSite', '0008_auto_20190608_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileapp',
            name='platform',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('ios', 'ios'), ('android', 'android')], max_length=7), size=2), blank=True, default=list, size=None),
        ),
    ]

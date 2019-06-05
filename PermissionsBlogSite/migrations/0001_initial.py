# Generated by Django 2.2.1 on 2019-06-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileAppType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MobileApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon', models.ImageField(upload_to='')),
                ('platform', models.CharField(choices=[('i', 'ios'), ('a', 'android')], max_length=1)),
                ('type', models.ManyToManyField(to='PermissionsBlogSite.MobileAppType')),
            ],
        ),
    ]
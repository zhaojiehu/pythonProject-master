# Generated by Django 3.2.19 on 2023-06-09 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20230608_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='academy_id',
        ),
    ]
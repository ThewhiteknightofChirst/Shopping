# Generated by Django 3.1.7 on 2021-05-19 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_remove_table_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='is_manager',
            field=models.BooleanField(default=True),
        ),
    ]

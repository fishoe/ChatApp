# Generated by Django 3.1 on 2020-08-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 2.0.7 on 2018-07-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rorender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='running',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 2.0.7 on 2018-07-11 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rorender', '0008_machine_is_workstation'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
    ]

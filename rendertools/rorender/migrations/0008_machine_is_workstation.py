# Generated by Django 2.0.7 on 2018-07-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rorender', '0007_machine_rendering'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='is_workstation',
            field=models.BooleanField(default=False),
        ),
    ]

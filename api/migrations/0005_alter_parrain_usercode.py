# Generated by Django 3.2.8 on 2021-10-26 07:47

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_campaign_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parrain',
            name='userCode',
            field=models.CharField(default=api.models.RandomID, editable=False, max_length=6, unique=True),
        ),
    ]

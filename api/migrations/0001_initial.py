# Generated by Django 3.2.8 on 2021-10-25 18:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='1234', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Parrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=60)),
                ('lastName', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('userCode', models.CharField(max_length=60)),
                ('addDate', models.DateField(default=datetime.date.today)),
                ('visits', models.IntegerField(default=0)),
                ('buy', models.IntegerField(default=0)),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.campaign')),
                ('step', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.steps')),
            ],
        ),
    ]

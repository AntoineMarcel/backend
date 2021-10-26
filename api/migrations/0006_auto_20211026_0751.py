# Generated by Django 3.2.8 on 2021-10-26 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_parrain_usercode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parrain',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.campaign'),
        ),
        migrations.AlterField(
            model_name='parrain',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.steps'),
        ),
        migrations.AlterField(
            model_name='steps',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.campaign'),
        ),
    ]

# Generated by Django 3.1.6 on 2021-02-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_terminal', '0007_alert_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert_report',
            name='SW',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='alert_report',
            name='TS',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='alert_report',
            name='Ping_Status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

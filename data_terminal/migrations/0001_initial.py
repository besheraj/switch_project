# Generated by Django 3.1.6 on 2021-02-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_terminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SW', models.IntegerField()),
                ('T1', models.IntegerField()),
                ('T3', models.IntegerField()),
                ('T4', models.IntegerField()),
                ('T5', models.IntegerField()),
                ('TS', models.IntegerField()),
            ],
        ),
    ]

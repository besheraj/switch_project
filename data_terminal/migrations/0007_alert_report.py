# Generated by Django 3.1.6 on 2021-02-07 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_terminal', '0006_auto_20210205_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ping_Status', models.CharField(max_length=20)),
                ('Status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data_terminal.data_terminal')),
            ],
        ),
    ]

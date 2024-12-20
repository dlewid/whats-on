# Generated by Django 5.1.2 on 2024-11-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team', models.CharField(default='none', max_length=200)),
                ('away_team', models.CharField(default='none', max_length=200)),
                ('sport', models.CharField(default='none', max_length=200)),
                ('event_date', models.DateField(default='2020-01-01')),
                ('event_time', models.TimeField(default='00:00')),
            ],
            options={
                'db_table': 'events',
            },
        ),
    ]

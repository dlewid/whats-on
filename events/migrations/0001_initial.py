# Generated by Django 5.1.2 on 2024-10-24 19:37

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
                ('title', models.CharField(max_length=200)),
                ('sport_category', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]

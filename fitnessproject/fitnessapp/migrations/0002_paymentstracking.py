# Generated by Django 4.2.2 on 2024-05-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentsTracking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('plan', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('timestamp', models.CharField(max_length=100)),
            ],
        ),
    ]

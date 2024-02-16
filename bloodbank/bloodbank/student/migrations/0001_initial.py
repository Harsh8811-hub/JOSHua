# Generated by Django 4.2.7 on 2023-11-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HospitalName', models.CharField(default='', max_length=100)),
                ('Address', models.CharField(default='', max_length=10)),
                ('ContactNumber', models.CharField(default='', max_length=10)),
                ('Website', models.CharField(default='', max_length=20)),
            ],
        ),
    ]

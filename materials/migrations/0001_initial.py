# Generated by Django 2.2.5 on 2019-09-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('order_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

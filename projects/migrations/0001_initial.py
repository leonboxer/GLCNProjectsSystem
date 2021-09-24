# Generated by Django 3.2.3 on 2021-05-26 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_number', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('elements', models.ManyToManyField(related_name='projects', to='elements.Element')),
                ('machinery_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.machinerytype')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]

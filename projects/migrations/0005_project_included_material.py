# Generated by Django 2.0.13 on 2019-08-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_auto_20190814_1335'),
        ('projects', '0004_project_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='included_material',
            field=models.ManyToManyField(related_name='project_included_material', to='materials.Material'),
        ),
    ]

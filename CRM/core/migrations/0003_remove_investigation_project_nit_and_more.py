# Generated by Django 4.2.5 on 2023-11-08 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_investigation_project_nit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investigation_project',
            name='nit',
        ),
        migrations.AddField(
            model_name='investigation_project',
            name='sponsors',
            field=models.ManyToManyField(related_name='projects', to='core.sponsor'),
        ),
    ]
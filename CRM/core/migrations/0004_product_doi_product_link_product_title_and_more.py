# Generated by Django 4.2.5 on 2023-11-13 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_investigation_project_nit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='doi',
            field=models.TextField(default='Not defined', unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.TextField(default='Not defined'),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.TextField(default='Not defined'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Journal', 'Paper de journal'), ('Congreso', 'Paper de congreso')], default='Journal', max_length=20),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_sponsor_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='id',
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='nit',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-15 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_sponsor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='status',
            field=models.CharField(max_length=10),
        ),
    ]

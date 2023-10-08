# Generated by Django 4.2.5 on 2023-10-08 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_donation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('Type1', 'Type1'), ('Type2', 'Type2'), ('Type3', 'Type3')], default='Type1', max_length=20)),
            ],
        ),
    ]

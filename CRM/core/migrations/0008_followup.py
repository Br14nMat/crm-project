# Generated by Django 4.2.5 on 2023-10-02 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_initialdonation_sponsor_initial_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.event')),
            ],
        ),
    ]

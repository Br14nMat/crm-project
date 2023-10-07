# Generated by Django 4.2.5 on 2023-10-02 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_initialdonation_sponsor_initial_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=3, max_digits=19)),
                ('date', models.DateField(auto_now_add=True)),
                ('type', models.CharField(choices=[('Type1', 'Type1'), ('Type2', 'Type2'), ('Type3', 'Type3')], default='Type1', max_length=20)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='core.sponsor')),
            ],
        ),
    ]
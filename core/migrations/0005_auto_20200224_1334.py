# Generated by Django 3.0.2 on 2020-02-24 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.City'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Job'),
        ),
    ]

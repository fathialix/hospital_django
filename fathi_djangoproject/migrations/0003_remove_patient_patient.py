# Generated by Django 4.1.7 on 2023-03-10 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fathi_djangoproject', '0002_patient_delete_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patient',
        ),
    ]
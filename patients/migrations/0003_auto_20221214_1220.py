# Generated by Django 2.2.3 on 2022-12-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20220811_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsymptomsanalysis',
            name='createdon',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

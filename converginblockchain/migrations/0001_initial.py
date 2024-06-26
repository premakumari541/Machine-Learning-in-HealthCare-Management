# Generated by Django 2.2.3 on 2022-12-14 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='docotrtregistrationmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=100)),
                ('loginid', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('authkey', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='patientregistrationmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('loginid', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('authkey', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
# Generated by Django 3.2.2 on 2021-08-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0011_remove_contactus_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carloaneligibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bangladeshi', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('net_income', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]

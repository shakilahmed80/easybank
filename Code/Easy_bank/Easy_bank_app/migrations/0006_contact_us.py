# Generated by Django 3.2.2 on 2021-05-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0005_credit_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=11)),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]

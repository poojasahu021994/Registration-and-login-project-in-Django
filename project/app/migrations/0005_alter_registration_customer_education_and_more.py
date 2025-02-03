# Generated by Django 5.1.5 on 2025-01-31 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_registration_customer_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='customer_Education',
            field=models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('P.Hd', 'P.Hd')], max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='customer_Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50),
        ),
    ]

# Generated by Django 5.0.6 on 2024-09-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]

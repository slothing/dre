# Generated by Django 2.0.4 on 2018-07-29 04:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('employee', '0008_auto_20180727_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='nik',
            field=models.CharField(blank=True, default='999999', max_length=10, unique=True),
        ),
    ]

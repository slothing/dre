# Generated by Django 2.0.4 on 2018-04-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('employee', '0003_auto_20180415_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='result',
            name='result',
            field=models.CharField(choices=[('productive', 'Produktif'), ('not-productive', 'Tidak Produktif')],
                                   default='not-productive', max_length=100),
        ),
    ]
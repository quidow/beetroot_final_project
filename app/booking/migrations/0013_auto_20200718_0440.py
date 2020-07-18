# Generated by Django 3.0.7 on 2020-07-18 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_auto_20200709_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomprice',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AddConstraint(
            model_name='roomprice',
            constraint=models.UniqueConstraint(fields=('room', 'date'), name='unique room and date'),
        ),
    ]

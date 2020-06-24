# Generated by Django 3.0.7 on 2020-06-24 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20200624_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomphoto',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.Hotel', verbose_name='Отель'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='persons',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Количество человек'),
        ),
    ]

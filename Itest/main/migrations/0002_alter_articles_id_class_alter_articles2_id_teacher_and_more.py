# Generated by Django 4.1 on 2022-09-03 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='id_class',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='id_класса'),
        ),
        migrations.AlterField(
            model_name='articles2',
            name='id_teacher',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='id_учителя'),
        ),
        migrations.AlterField(
            model_name='articles3',
            name='id_subject',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='id предмета'),
        ),
    ]

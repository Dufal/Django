# Generated by Django 4.1.5 on 2023-01-24 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_contract_personal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='data_okonchanie',
            field=models.DateField(null=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='data_zukluchenie',
            field=models.DateField(null=True, verbose_name='Дата заключения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='home_phone_number',
            field=models.IntegerField(blank=True, verbose_name='Домашний телефон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport_number',
            field=models.IntegerField(verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(max_length=40, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='self_phone_number',
            field=models.IntegerField(blank=True, verbose_name='Личный номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=40, verbose_name='Фамилия'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-21 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.contract'),
        ),
    ]
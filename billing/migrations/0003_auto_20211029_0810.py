# Generated by Django 3.2.8 on 2021-10-29 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20211029_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='tax',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bill',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bill',
            name='total_wo_tax',
            field=models.IntegerField(default=0),
        ),
    ]
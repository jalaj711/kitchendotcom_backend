# Generated by Django 3.2.7 on 2021-10-12 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20211011_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kitchenimage',
            options={'verbose_name': 'Kitchen Image', 'verbose_name_plural': 'Kitchen Images'},
        ),
        migrations.AlterField(
            model_name='kitchenimage',
            name='kitchen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details'),
        ),
        migrations.AlterModelTable(
            name='kitchenimage',
            table=None,
        ),
        migrations.CreateModel(
            name='KitchenVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos/kitchen/')),
                ('kitchen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
            options={
                'verbose_name': 'Kitchen Video',
                'verbose_name_plural': 'Kitchen Videos',
            },
        ),
    ]

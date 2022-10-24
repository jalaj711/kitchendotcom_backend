# Generated by Django 3.2.7 on 2021-10-13 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20211013_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='kitchen',
        ),
        migrations.DeleteModel(
            name='City1',
        ),
        migrations.DeleteModel(
            name='City10',
        ),
        migrations.DeleteModel(
            name='City11',
        ),
        migrations.DeleteModel(
            name='City12',
        ),
        migrations.DeleteModel(
            name='City13',
        ),
        migrations.DeleteModel(
            name='City2',
        ),
        migrations.DeleteModel(
            name='City3',
        ),
        migrations.DeleteModel(
            name='City4',
        ),
        migrations.DeleteModel(
            name='City5',
        ),
        migrations.DeleteModel(
            name='City6',
        ),
        migrations.DeleteModel(
            name='City7',
        ),
        migrations.DeleteModel(
            name='City8',
        ),
        migrations.DeleteModel(
            name='City9',
        ),
        migrations.DeleteModel(
            name='Other',
        ),
        migrations.CreateModel(
            name='City1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('Status', models.CharField(choices=[('New', 'New'), ('Follow Up', 'Follow Up'), ('Project Started', 'Project Started'), ('Project Completed', 'Project Completed'), ('Declined', 'Declined')], default='New', max_length=50)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
            options={
                'verbose_name': 'Varanasi kitchen',
            },
        ),
        migrations.CreateModel(
            name='City10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='City11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='City12',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='City13',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='City2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
            options={
                'verbose_name': 'Chandauli kitchen',
            },
        ),
        migrations.CreateModel(
            name='City3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='City4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='City5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='City6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='City7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='City8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='City9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('Location', models.CharField(default='NA', max_length=12)),
                ('kitchen', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.kitchen_details')),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
# Generated by Django 3.1.3 on 2021-09-19 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_rename_post_postimage_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='project_name',
            field=models.TextField(default='Project', max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user_name',
            field=models.TextField(default='Client', max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='video',
            field=models.FileField(default='NA', upload_to='feedbacks/vid'),
        ),
        migrations.AlterField(
            model_name='design',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default='NA', max_length=1000),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

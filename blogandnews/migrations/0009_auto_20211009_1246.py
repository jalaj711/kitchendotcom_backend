# Generated by Django 3.2.7 on 2021-10-09 12:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogandnews', '0008_merge_0006_auto_20210930_1405_0007_auto_20211002_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='sno',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='author',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.c_details'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='id',
            field=models.BigAutoField(
                auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

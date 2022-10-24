# Generated by Django 3.2.8 on 2021-10-29 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franch_name', models.CharField(max_length=100)),
                ('franch_address', models.CharField(max_length=100)),
                ('franch_gst', models.CharField(max_length=100)),
                ('franch_state', models.CharField(max_length=100)),
                ('franch_statecode', models.CharField(max_length=100)),
                ('franch_mail', models.CharField(max_length=100)),
                ('ship_name', models.CharField(max_length=100)),
                ('ship_address', models.CharField(max_length=100)),
                ('ship_gst', models.CharField(max_length=100)),
                ('ship_state', models.CharField(max_length=100)),
                ('ship_statecode', models.CharField(max_length=100)),
                ('bill_name', models.CharField(max_length=100)),
                ('bill_address', models.CharField(max_length=100)),
                ('bill_gst', models.CharField(max_length=100)),
                ('bill_state', models.CharField(max_length=100)),
                ('bill_statecode', models.CharField(max_length=100)),
                ('invoice_no', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('delivery_note', models.CharField(max_length=100)),
                ('payment_mode', models.CharField(max_length=100)),
                ('ref_no', models.CharField(max_length=100)),
                ('other_ref', models.CharField(max_length=100)),
                ('buy_ord_no', models.CharField(max_length=100)),
                ('buy_dated', models.CharField(max_length=100)),
                ('dispatch_date', models.CharField(max_length=100)),
                ('delivery_date', models.CharField(max_length=100)),
                ('dispatch_through', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('delivery_terms', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('hsn', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('per', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('remarks', models.TextField(max_length=500)),
                ('_for', models.TextField(max_length=500)),
            ],
        ),
    ]
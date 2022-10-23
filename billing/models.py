from django.db import models


class Bill(models.Model):
    franch_name = models.CharField(max_length=100, )
    franch_address = models.CharField(max_length=100, )
    franch_gst = models.CharField(max_length=100, )
    franch_state = models.CharField(max_length=100, )
    franch_statecode = models.CharField(max_length=100, )
    franch_mail = models.CharField(max_length=100, )

    ship_name = models.CharField(max_length=100, )
    ship_address = models.CharField(max_length=100, )
    ship_gst = models.CharField(max_length=100, )
    ship_state = models.CharField(max_length=100, )
    ship_statecode = models.CharField(max_length=100, )

    bill_name = models.CharField(max_length=100, )
    bill_address = models.CharField(max_length=100, )
    bill_gst = models.CharField(max_length=100, )
    bill_state = models.CharField(max_length=100, )
    bill_statecode = models.CharField(max_length=100, )

    invoice_no = models.CharField(max_length=100, )
    date = models.CharField(max_length=100, )
    delivery_note = models.CharField(max_length=100, )
    payment_mode = models.CharField(max_length=100, )
    ref_no = models.CharField(max_length=100, )
    other_ref = models.CharField(max_length=100, )
    buy_ord_no = models.CharField(max_length=100, )
    buy_dated = models.CharField(max_length=100, )
    dispatch_date = models.CharField(max_length=100, )
    delivery_date = models.CharField(max_length=100, )
    dispatch_through = models.CharField(max_length=100, )
    destination = models.CharField(max_length=100, )
    delivery_terms = models.CharField(max_length=100, )

    total = models.IntegerField(default=0)
    total_wo_tax = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)

    remarks = models.TextField(max_length=500, )
    _for = models.TextField(max_length=500, )

    def __str__(self) -> str:
        if len(self.invoice_no) == 0:
            return 'no ivoince no'
        else:
            return self.invoice_no


class Bill_Item(models.Model):
    bill = models.ForeignKey("Bill", verbose_name=("items of bills"),
                             on_delete=models.CASCADE)
    item = models.CharField(max_length=100, )
    hsn = models.CharField(max_length=100, )
    quantity = models.CharField(max_length=100, )
    rate = models.CharField(max_length=100, )
    per = models.CharField(max_length=100, )
    amount = models.IntegerField()
    tax = models.IntegerField()

    def __str__(self) -> str:
        return self.hsn

from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from billing.models import Bill, Bill_Item

import inflect
num2words = inflect.engine()


@staff_member_required
def billing(request):
    if request.method == "POST":
        context_invoice = {
            'franch_name': request.POST.get('franch_name'),
            'franch_address': request.POST.get('franch_address'),
            'franch_gst': request.POST.get('franch_gst'),
            'franch_state': request.POST.get('franch_state'),
            'franch_statecode': request.POST.get('franch_gst')[0:2],
            'franch_mail': request.POST.get('franch_mail'),

            'ship_name': request.POST.get('ship_name'),
            'ship_address': request.POST.get('ship_address'),
            'ship_gst': request.POST.get('ship_gst'),
            'ship_state': request.POST.get('ship_state'),
            'ship_statecode': request.POST.get('ship_gst')[0:2],

            'bill_name': request.POST.get('bill_name'),
            'bill_address': request.POST.get('bill_address'),
            'bill_gst': request.POST.get('bill_gst'),
            'bill_state': request.POST.get('bill_state'),
            'bill_statecode': request.POST.get('bill_gst')[0:2],

            'invoice_no': request.POST.get('invoice_no'),
            'date': request.POST.get('date'),
            'delivery_note': request.POST.get('delivery_note'),
            'payment_mode': request.POST.get('payment_mode'),
            'ref_no': request.POST.get('ref_no'),
            'other_ref': request.POST.get('other_ref'),
            'buy_ord_no': request.POST.get('buy_ord_no'),
            'buy_dated': request.POST.get('buy_dated'),
            'dispatch_date': request.POST.get('dispatch_date'),
            'delivery_date': request.POST.get('delivery_date'),
            'dispatch_through': request.POST.get('dispatch_through'),
            'destination': request.POST.get('destination'),
            'delivery_terms': request.POST.get('delivery_terms'),

            'item': request.POST.getlist('item'),
            'hsn': request.POST.getlist('hsn'),
            'quantity': request.POST.getlist('quantity'),
            'rate': request.POST.getlist('rate'),
            'per': request.POST.getlist('per'),
            'amount': request.POST.getlist('amount'),

            'remarks': request.POST.get('remarks'),
            'for': request.POST.get('for'),
            # 'taxs': [],
        }

        bill_obj_value = {
            'franch_name': request.POST.get('franch_name'),
            'franch_address': request.POST.get('franch_address'),
            'franch_gst': request.POST.get('franch_gst'),
            'franch_state': request.POST.get('franch_state'),
            'franch_statecode': request.POST.get('franch_gst')[0:2],
            'franch_mail': request.POST.get('franch_mail'),

            'ship_name': request.POST.get('ship_name'),
            'ship_address': request.POST.get('ship_address'),
            'ship_gst': request.POST.get('ship_gst'),
            'ship_state': request.POST.get('ship_state'),
            'ship_statecode': request.POST.get('ship_gst')[0:2],

            'bill_name': request.POST.get('bill_name'),
            'bill_address': request.POST.get('bill_address'),
            'bill_gst': request.POST.get('bill_gst'),
            'bill_state': request.POST.get('bill_state'),
            'bill_statecode': request.POST.get('bill_gst')[0:2],

            'invoice_no': request.POST.get('invoice_no'),
            'date': request.POST.get('date'),
            'delivery_note': request.POST.get('delivery_note'),
            'payment_mode': request.POST.get('payment_mode'),
            'ref_no': request.POST.get('ref_no'),
            'other_ref': request.POST.get('other_ref'),
            'buy_ord_no': request.POST.get('buy_ord_no'),
            'buy_dated': request.POST.get('buy_dated'),
            'dispatch_date': request.POST.get('dispatch_date'),
            'delivery_date': request.POST.get('delivery_date'),
            'dispatch_through': request.POST.get('dispatch_through'),
            'destination': request.POST.get('destination'),
            'delivery_terms': request.POST.get('delivery_terms'),

            'remarks': request.POST.get('remarks'),
            '_for': request.POST.get('for'),
            # 'taxs': [],
        }
        bill = Bill(**bill_obj_value)
        bill.save()

        # context_invoice['amount'] = context_invoice['quantity'] / \
        # context_invoice['per']*context_invoice['rate']

        # tax = round(int(context_invoice['amount']) * 0.18, 2)

        total_tax = 0
        total_amount = 0
        total_wo_tax = 0
        items = []

        for (item, hsn, quan, rate, per,) in zip(context_invoice['item'],
                                                 context_invoice['hsn'],
                                                 context_invoice['quantity'],
                                                 context_invoice['rate'],
                                                 context_invoice['per'],):
            if (
                    quan == 0
            ):
                continue
            amount = 0
            amount = (int(quan)/int(per))*int(rate)
            total_wo_tax += amount
            tax = round(amount*0.18, 2)
            tax_amount = amount + tax
            total_tax += tax
            total_amount += tax_amount

            item = {
                'item': item,
                'hsn': hsn,
                'quantity': quan,
                'rate': rate,
                'per': per,
                'amount': amount,
                'tax': tax,
            }
            items.append(item)
            bill_item = Bill_Item(bill=bill, **item)
            bill_item.save()

        if context_invoice['franch_statecode'] == context_invoice['bill_statecode']:
            context_invoice['taxs'] = [
                {'type': 'cgst', 'rate': '9', 'amount': total_tax/2},
                {'type': 'sgst', 'rate': '9', 'amount': total_tax/2}
            ]
            print('yes')
        else:
            context_invoice['taxs'] = [
                {'type': 'igst', 'rate': '18', 'amount': total_tax}
            ]
            print('no')

        context_invoice['items'] = items
        context_invoice['total'] = total_amount
        context_invoice['total_wo_tax'] = total_wo_tax

        context_invoice['total_charge_words'] = num2words.number_to_words(
            int(total_amount))
        context_invoice['tax'] = total_tax
        context_invoice['total_tax_words'] = num2words.number_to_words(
            total_tax
        )
        request.session['context_invoice'] = context_invoice

        bill.total = total_amount
        bill.total_wo_tax = total_wo_tax
        bill.tax = total_tax
        bill.save()

        return render(request, 'billing_output.html', context_invoice)

    return render(request, 'billing_form.html')

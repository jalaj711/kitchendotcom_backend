import json
from django.http.response import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
# importing calculation model is removed
from home.models import City11, City12, City13, Other, c_details, kitchen_details, Constant, City1, City2, City3, City4, City5, City6, City7, City8, City9, City10, TempLink
from home.forms import KitchenDetailsForm, KitchenImageFormSet, KitchenVideoFormSet
from datetime import datetime
from fpdf import FPDF
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


values = Constant.objects.all().last()
rate = {
    '1': {
        'Essentials': int(values.Essentials),
        'Premium': int(values.Premium),
        'Luxe': int(values.Luxe)},
    'Yes': int(values.countertop),
    'HDHMR': int(values.HDHMR),
    'MR Plywood': int(values.MR_Plywood),
    'BWR Plywood': int(values.BWR_Plywood),
    'BWP Plywood': int(values.BWP_Plywood),
    'Laminate': int(values.Laminate),
    'PVC Laminate': int(values.PVC_Laminate),
    'Anti-scratch Acrylic': int(values.Anti_scratch_Acrylic),
    'Glossy PU': int(values.Glossy_PU),
    'Basic': int(values.Basic_Acc),
    'Intermediate': int(values.Intermediate_Acc),
    'Premium': int(values.Prem_Acc)
}

# Your views here.


def landing_page(request):
    return render(request, 'landing_page.html')


def contact_us(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('first_name') + " " + data.get('last_name')
        email = data.get('email')
        location = data.get('city')
        message = data.get('message')
        details = c_details(name=name, email=email,
                            location=location, message=message)
        details.save()
        return JsonResponse({
            'success': True
        })
    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response


def about_us(request):
    return render(request, "about_us.html")


def project_gallery(request):
    return render(request, 'project_gallery.html')


def design_gallery(request):
    return render(request, 'design_gallery.html')


def kitchen_price_steps(request):
    # request.session['name'] = 'test'
    return render(request, 'kitchen_price_steps.html')


def select_layout(request):
    if request.method == "POST":
        data = json.loads(request.body)
        layout = data.get('kitchenLayout')
        request.session['layout'] = layout
        return JsonResponse({
            'success': True,
            'next': '/estimator/customer-details'
        })

    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response


def customer_details(request):
    layout = request.session.get('layout')
    # store the choise and details of customer here
    # context = kitchen_details.objects.all().last()
    # selected_layout = sizeof(context)
    # print(type(selected_layout))
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        location1 = data.get('location')
        # print(location1)
        request.session['name'] = name
        request.session['email'] = email
        request.session['phone'] = phone
        request.session['location'] = location1

        c_detail = c_details(name=name, email=email,
                             phone=phone, location=location1)
        c_detail.save()
        next_page = ''
        if layout == "L-Shaped":
            next_page = '/estimator/select-dimensions/l-shape'
        elif (layout == 'Straight'):
            next_page = '/estimator/select-dimensions/straight-shape'
        elif (layout == 'U-Shaped'):
            next_page = '/estimator/select-dimensions/u-shape'
        elif (layout == 'Parallel'):
            next_page = '/estimator/select-dimensions/parallel-shape'
        return JsonResponse({
            'success': True,
            'next': next_page
        })
    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response


def layout_dimensions(request):
    if request.method == "POST":
        data = json.loads(request.body)
        a_feet = data.get('a_feet')
        a_inch = data.get('a_inch')
        b_feet = data.get('b_feet')
        b_inch = data.get('b_inch')
        c_feet = data.get('c_feet')
        c_inch = data.get('c_inch')
        request.session['a_feet'] = a_feet
        request.session['a_inch'] = a_inch
        request.session['b_feet'] = b_feet
        request.session['b_inch'] = b_inch
        request.session['c_feet'] = c_feet
        request.session['c_inch'] = c_inch
        return JsonResponse({
            'success': True,
            'next': '/estimator/select-loft-type'
        })
    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response


def select_loft_type(request):

    if request.method == "POST":
        data = json.loads(request.body)
        loft1 = data.get('loft')
        request.session['loft'] = loft1
        return JsonResponse({
            'success': True,
            'next': '/select-package'
        })
    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response


def select_package(request):  # fqname is not confirmed

    # to be entered in following 4 function
    if request.method == "POST":
        # "package" <- this name might be different

        data = json.loads(request.body)
        package = data.get('package')
        request.session['package'] = package

        if package == "Build your own package":
            return JsonResponse({
                'success': True,
                'next': '/build_package'
            })
        if package == "Essentials":
            request.session['material'] = "MR Plywood"
            request.session['finish'] = "Laminate"
            request.session['accessories'] = "Wire Basket"
            request.session['countertop'] = "no"
        if package == "Premium":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "PVC"
            request.session['accessories'] = "Tandem Basket"
            request.session['countertop'] = "no"
        if package == "Luxe":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "Acrylic"
            request.session['accessories'] = "Tandem Basket"
            request.session['countertop'] = "no"
        return JsonResponse({
            'success': True,
            'next': '/summary'
        })

    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response

def build_package(request):
    if request.method == "POST":
        data = json.loads(request.body)
        material = data.get('ownpackage')
        request.session['material'] = material
        return JsonResponse({
            'success': True,
            'next': '/select_countertop'
        })

    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response

def select_countertop(request):
    if request.method == "POST":
        data = json.loads(request.body)
        c_top = data.get('countertop')
        request.session['countertop'] = c_top
        return JsonResponse({
            'success': True,
            'next': '/select_finish'
        })

    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response

def select_finish(request):
    if request.method == "POST":
        data = json.loads(request.body)
        request.session['finish'] = data.get('finish')
        return JsonResponse({
            'success': True,
            'next': '/estimator/select-accessories'
        })
    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response


def select_accessories(request):
    if request.method == "POST":
        data = json.loads(request.body)
        acc = data.get('accessories')
        request.session['accessories'] = acc
        return JsonResponse({
            'success': True,
            'next': '/estimator/select-services'
        })
    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response

def select_services(request):
    if request.method == "POST":
        data = json.loads(request.body)
        services_list = data.get('services')
        request.session['services'] = services_list
        return JsonResponse({
            'success': True,
            'next': '/estimator/select-appliances'
        })
    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response


def select_appliances(request):
    if request.method == "POST":
        data = json.loads(request.body)
        app_list = data.get('appliances')
        # print(app_list)
        request.session['appliances'] = app_list
        return JsonResponse({
            'success': True,
            'next': '/summary/buildpkg'
        })
    response = HttpResponse("Method not allowed", status=405)
    response["Allow"] = "POST"
    return response


def kitchen_summary(request):

    # constant = Constant.objects.all().last()
    # key names are as per summary page
    context = {
        'name': request.session.get('name'),
        'phone': request.session.get('phone'),
        'email': request.session.get('email'),
        'shape': request.session.get('layout'),
        'a_feet': request.session.get('a_feet'),
        'a_inch': request.session.get('a_inch'),
        'b_feet': request.session.get('b_feet'),
        'b_inch': request.session.get('b_inch'),
        'c_feet': request.session.get('c_feet'),
        'c_inch': request.session.get('c_inch'),
        # 'name': request.session.get('name'),
        'loft': request.session.get('loft'),
        'type': request.session.get('package'),
        'material': request.session.get('material'),
        'finish': request.session.get('finish'),
        'accessories': request.session.get('accessories'),
        'location': request.session.get('location'),
    }

    # context['countertop'] = False

    # Calculation part begins
    a = round(int(context['a_feet']) + (int(context['a_inch']) / 12), 2)
    b = round(int(context['b_feet']) + (int(context['b_inch']) / 12), 2)
    c = round(int(context['c_feet']) + (int(context['c_inch']) / 12), 2)
    l = int(context['loft'])

    # last value should be fetched from mode
    cal = round(((a+b+c) * (3+l) * rate['1'][context['type']]), 2)
    pdf_variable = rate['1'][context['type']]
    # Calculation part ends
    size = str(round(a, 2)) + "ft x " + str(round(b, 2)) + \
        "ft x " + str(round(c, 2)) + "ft"
    # Saving data in main table
    details = kitchen_details(Phone=context['phone'], Name=context['name'], Email=context['email'], Shape=context['shape'], Size=size, Loft=context['loft'], Type=context['type'],
                              Accessories=context['accessories'], Material=context['material'], Finish=context['finish'], Price=cal, Location=context['location'], date=datetime.today())
    details.save()

    # Saving data in specific location table
    city = {
        'Varanasi': City1(),
        'Chandauli': City2(),
        'Mirzapur': City3(),
        'Sonbhadra': City4(),
        'Ayodhya': City5(),
        'Prayagraj': City6(),
        'Lucknow': City7(),
        'Bhadohi': City8(),
        'Gorakhpur': City9(),
        'Ghazipur': City10(),
        'Azamgarh': City11(),
        'Kanpur': City12(),
        'Jaunpur': City13(),
        'Other': Other()
        # 'Ghazipur' : City10(Phone = details, Shape = context['shape'], Size = size, Loft = context['loft'], Type = context['type'], Accessories = context['accessories'], Material = context['material'], Finish = context['finish'],Price = cal, Location = context['location'], date = datetime.today()),
        # 'Azamgarh' :City10(Phone = details, Shape = context['shape'], Size = size, Loft = context['loft'], Type = context['type'], Accessories = context['accessories'], Material = context['material'], Finish = context['finish'],Price = cal, Location = context['location'], date = datetime.today()),
        # 'Kanpur' : City10(Phone = details, Shape = context['shape'], Size = size, Loft = context['loft'], Type = context['type'], Accessories = context['accessories'], Material = context['material'], Finish = context['finish'],Price = cal, Location = context['location'], date = datetime.today()),
        # 'Jaunpur' : City10(Phone = details, Shape = context['shape'], Size = size, Loft = context['loft'], Type = context['type'], Accessories = context['accessories'], Material = context['material'], Finish = context['finish'],Price = cal, Location = context['location'], date = datetime.today())
    }
    city_obj = city[request.session.get('location')]
    city_obj.kitchen = details
    city_obj.save()

    context['size'] = size
    context['price'] = cal
    context['loft'] = request.session.get('loft') + ' feet loft'
    date = datetime.now().date()

    pdf = FPDF()
    pdf.add_page()
    pdf.image("static/pdf/bg_1.png", 0, 0, 210, 297, 'png')  # Background image
    pdf.image("static/pdf/Group.png", 100, 10)  # logo
    pdf.set_text_color(0, 102, 101)
    pdf.set_font("Arial", size=20)
    pdf.cell(190, 40, "Kitchendotcom", ln=1, align="C")

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 8, "Name : ", ln=0, align="L")
    pdf.cell(20, 8, request.session.get('name'), ln=1, align="L")
    pdf.cell(40, 8, "Address : ", ln=0, align="L")
    pdf.cell(20, 8, request.session.get('location'), ln=1, align="L")
    pdf.cell(40, 8, "Contact No. : ", ln=0, align="L")
    pdf.cell(20, 8, request.session.get('phone'), ln=1, align="L")

    pdf.multi_cell(0, 10, "", align="L")

    pdf.set_fill_color(255, 255, 255)
    pdf.cell(190, 10, ln=1, border="L"+"T"+"R", fill=1)
    pdf.cell(190, 10, " Kitchendotcom", ln=1, border="L"+"R", align="L")
    pdf.cell(40, 10, " Address : ", ln=0, border="L", align="L", fill=1)
    pdf.cell(150, 10, "D65/245 Lahartara , Varanasi",
             ln=1, border="R", align="L", fill=1)
    pdf.cell(40, 10, " Date : ", ln=0, border="L"+"B", align="L")
    pdf.cell(150, 10, str(date), ln=1, border="B"+"R", align="L")

    pdf.set_font("Arial", size=15)
    pdf.cell(190, 20, "Quotation", ln=1, align="C")

    pdf.set_font("Arial", size=10)
    pdf.cell(30, 15, "Sr.No.", ln=0, border="L"+"T", align="C", fill=1)
    pdf.cell(40, 15, "Particulars", ln=0, border="T", align="L", fill=1)
    pdf.cell(40, 15, "Rate", ln=0, border="T", align="L", fill=1)
    pdf.cell(40, 15, "Sqft.", ln=0, border="T", align="L", fill=1)
    pdf.cell(40, 15, "Amount", ln=1, border="T"+"R", align="L", fill=1)
    pdf.cell(30, 10, "1.", ln=0, border="L", align="C", fill=1)
    pdf.cell(40, 10, "Plan Deisgning", ln=0, border="", align="L", fill=1)
    pdf.cell(40, 10, str(3*pdf_variable), ln=0, border="", align="L", fill=1)
    pdf.cell(40, 10, str(a+b+c), ln=0, border="", align="L", fill=1)
    pdf.cell(40, 10, str(round((a+b+c) * 3 * pdf_variable, 2)),
             ln=1, border="R", align="L", fill=1)
    # pdf.set_fill_color(0,102,101)
    pdf.cell(30, 10, "2.", ln=0, border="L", align="C")
    pdf.cell(40, 10, "Loft", ln=0, border="", align="L")
    pdf.cell(40, 10, str(l * pdf_variable), ln=0, border="", align="L")
    pdf.cell(40, 10, str(a+b+c), ln=0, border="", align="L")
    pdf.cell(40, 10, str(round((l * pdf_variable * (a+b+c)), 2)),
             ln=1, border="R", align="L")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(190, 10, "", ln=1, border="L"+"R", align="C", fill=1)
    # pdf.set_fill_color(0,102,101)
    pdf.cell(190, 10, "", ln=1, border="L"+"R", align="C")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(10, 20, "", ln=0, border="L"+"B", fill=1)
    pdf.cell(140, 20, "Total", ln=0, border="B", align="L", fill=1)
    pdf.cell(40, 20, str(cal), ln=1, border="B"+"R", align="L", fill=1)

    pdf.multi_cell(0, 5, "", align="L")
    pdf.cell(200, 6, "Terms & Conditions :-", ln=1, align="L")
    pdf.set_font("Arial", size=8)
    pdf.cell(
        200, 4, "1. Above quotation is just for noted job works/Materials.", ln=1, align="L")
    pdf.cell(
        200, 4, "2. Payment is expected Either in Cash or Account transfer", ln=1, align="L")
    pdf.cell(200, 4, "3. No hidden costs further of any kind of expenses likeDesigning, transportation or installation,etc in case of turnkey.", ln=1, align="L")
    pdf.cell(200, 4, "4. Offers/schemes are marked as*For Free*.", ln=1, align="L")
    pdf.cell(200, 4, "5. Appliances and Services(Ceiling light, Civil work,Plumbing and Flooring) are not counted in above quotaion i.e. it will be quoted as per selection", ln=1, align="L")
    pdf.cell(
        200, 4, "6. Payment Schedule as prescribed by area manager.", ln=1, align="L")

    pdf.add_page()
    pdf.image("static/pdf/bg_2.png", 0, 0, 210, 297, 'png')
    pdf.set_font("Arial", size=15)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(190, 15, "Summary", ln=1, align="C")

    pdf.set_font("Arial", size=10)
    pdf.cell(10, 15, "", ln=0, border="L"+"T", fill=1)
    pdf.cell(50, 15, "Sr.No.", ln=0, border="T", align="L", fill=1)
    pdf.cell(130, 15, "Particulars", ln=1, border="T"+"R", align="L", fill=1)
    pdf.cell(30, 10, "1.", ln=0, border="L", align="C", fill=1)
    pdf.cell(80, 10, "Shape", ln=0, border="", align="C", fill=1)
    pdf.cell(80, 10, request.session.get('layout'),
             ln=1, border="R", align="C", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.cell(30, 10, "2.", ln=0, border="L", align="C")
    pdf.cell(80, 10, "Size", ln=0, border="", align="C")
    pdf.cell(80, 10, str(a+b+c), ln=1, border="R", align="C")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(30, 10, "3.", ln=0, border="L", align="C", fill=1)
    pdf.cell(80, 10, "Type", ln=0, border="", align="C", fill=1)
    pdf.cell(80, 10, request.session.get('package'),
             ln=1, border="R", align="C", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.cell(30, 10, "4.", ln=0, border="L", align="C")
    pdf.cell(80, 10, "Material", ln=0, border="", align="C")
    pdf.cell(80, 10, request.session.get(
        'material'), ln=1, border="R", align="C")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(30, 10, "5.", ln=0, border="L", align="C", fill=1)
    pdf.cell(80, 10, "Countertop", ln=0, border="", align="C", fill=1)
    pdf.cell(80, 10, 'No',
             ln=1, border="R", align="C", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.cell(30, 10, "6.", ln=0, border="L", align="C")
    pdf.cell(80, 10, "Loft", ln=0, border="", align="C")
    pdf.cell(80, 10, request.session.get('loft'), ln=1, border="R", align="C")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(30, 10, "7.", ln=0, border="L", align="C", fill=1)
    pdf.cell(80, 10, "Finish", ln=0, border="", align="C", fill=1)
    pdf.cell(80, 10, request.session.get('finish'),
             ln=1, border="R", align="C", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.cell(30, 10, "8.", ln=0, border="L", align="C")
    pdf.cell(80, 10, "Accessories", ln=0, border="", align="C")
    pdf.cell(80, 10, request.session.get(
        'accessories'), ln=1, border="R", align="C")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 20, "Total", ln=0, border="L"+"B", align="R", fill=1)
    pdf.cell(135, 20, str(cal), ln=0, border="B", align="R", fill=1)
    pdf.cell(35, 20, "", ln=1, border="B"+"R", align="C", fill=1)

    pdf.set_font("Arial", size=15)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(190, 20, "Payment Schedule", ln=1, align="C")
    pdf.set_font("Arial", size=10)
    pdf.cell(35, 15, "  Sr.No.", ln=0, border="L"+"T", align="L", fill=1)
    pdf.cell(35, 15, "Date/Day", ln=0, border="T", align="L", fill=1)
    pdf.cell(35, 15, "Paid By", ln=0, border="T", align="L", fill=1)
    pdf.cell(35, 15, "Amount", ln=0, border="T", align="L", fill=1)
    pdf.cell(50, 15, "Mode of Payment", ln=1,
             border="T"+"R", align="L", fill=1)
    pdf.multi_cell(190, 10, "   1.", border="L"+"R", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.multi_cell(190, 10, "   2.", border="L"+"R")
    pdf.set_fill_color(255, 255, 255)
    pdf.multi_cell(190, 10, "   3.", border="L"+"R", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.multi_cell(190, 10, "   4.", border="L"+"R")
    pdf.set_fill_color(255, 255, 255)
    pdf.multi_cell(190, 10, "   5.", border="L"+"R", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.multi_cell(190, 10, "   6.", border="L"+"R")
    pdf.set_fill_color(255, 255, 255)
    pdf.multi_cell(190, 10, "   7.", border="L"+"R", fill=1)
    # pdf.set_fill_color(0, 132, 153)
    pdf.multi_cell(190, 10, "   8.", border="L"+"R")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(190, 10, ln=1, border="L"+"B"+"R", fill=1)
    # Rows
    pdf.set_text_color(128, 128, 128)
    pdf.cell(200, 10, "www.kitchendotcom", ln=0, align="C")

    # request.session.session_key
    # request.session.get('name')
    file_name = "media/pdf/" + str(request.session.session_key)+".pdf"
    pdf.output(name=file_name)

    # os.remove(file_name)
    template = render_to_string('email_template.html', {
                                'name': request.session.get('name')})
    email = EmailMessage(
        'Modular Kitchen Estimate',
        template,
        settings.EMAIL_HOST_USER,
        [request.session.get('email')]
    )
    # name = request.session.get('name') + '_KichenEstimate.pdf'
    email.attach_file(file_name)
    email.fail_silently = True
    # email.send()
    return render(request, 'kitchen_summary.html', {'context': context})


def kitchen_summary_buildpkg(request):
    constant = Constant.objects.all().last()
    # key names are as per summary page
    context = {
        'phone': request.session.get('phone'),
        'email': request.session.get('email'),
        'shape': request.session.get('layout'),
        'name': request.session.get('name'),
        'a_feet': request.session.get('a_feet'),
        'a_inch': request.session.get('a_inch'),
        'b_feet': request.session.get('b_feet'),
        'b_inch': request.session.get('b_inch'),
        'c_feet': request.session.get('c_feet'),
        'c_inch': request.session.get('c_inch'),
        'loft': request.session.get('loft'),
        'type': request.session.get('package'),
        'material': request.session.get('material'),
        'countertop': request.session.get('countertop'),
        'finish': request.session.get('finish'),
        'accessories': request.session.get('accessories'),
        'services':  request.session.get('services'),
        'appliances':  request.session.get('appliances'),
        'location': request.session.get('location')
    }

    # Calculation part begins
    a = round(int(context['a_feet']) + (int(context['a_inch']) / 12), 2)
    b = round(int(context['b_feet']) + (int(context['b_inch']) / 12), 2)
    c = round(int(context['c_feet']) + (int(context['c_inch']) / 12), 2)
    l = int(context['loft'])

    size = str(round(a, 2)) + "ft x " + str(round(b, 2)) + \
        "ft x " + str(round(c, 2)) + "ft"
    # calculation of pricing
    if context['countertop'] == "Yes":
        cal = round(((a+b+c) * (3+l) * (rate[context['material']] + rate[context['finish']
                                                                         ] + rate[context['accessories']]) + rate[context['countertop']]), 2)
        pdf_variable = (rate[context['material']]+rate[context['finish']] +
                        rate[context['accessories']] + rate[context['countertop']])
    else:
        cal = round(((a+b+c) * (3+l) * (rate[context['material']] +
                    rate[context['finish']] + rate[context['accessories']])), 2)
        pdf_variable = (rate[context['material']] +
                        rate[context['finish']] + rate[context['accessories']])
    # Calculation part end

    details = kitchen_details(Phone=context['phone'], Name=context['name'], Email=context['email'], Shape=context['shape'], Size=size, Type=context['type'], Material=context['material'], Countertop=context['countertop'],
                              Loft=context['loft'], Finish=context['finish'], Accessories=context['accessories'], Appliances=context['appliances'], Services=context['services'], Price=cal, Location=context['location'], date=datetime.today())
    details.save()
    # Saving data in specific location table
    city = {
        'Varanasi': City1(),
        'Chandauli': City2(),
        'Mirzapur': City3(),
        'Sonbhadra': City4(),
        'Ayodhya': City5(),
        'Prayagraj': City6(),
        'Lucknow': City7(),
        'Bhadohi': City8(),
        'Gorakhpur': City9(),
        'Ghazipur': City10(),
        'Azamgarh': City11(),
        'Kanpur': City12(),
        'Jaunpur': City13(),
        'Other': Other()
        # 'Ghazipur' : City10(Phone = details, Shape = context['shape'], Size = size, Loft = context['loft'], Type = context['type'], Accessories = context['accessories'], Material = context['material'], Finish = context['finish'],Price = cal, Location = context['location'], date = datetime.today()),
        # 'Azamgarh' :City10(Phone = details, Shape = context['shape'], Size = size, Loft = context['loft'], Type = context['type'], Accessories = context['accessories'], Material = context['material'], Finish = context['finish'],Price = cal, Location = context['location'], date = datetime.today()),
        # 'Kanpur' : City10(Phone = details, Shape = context['shape'], Size = size, Loft = context['loft'], Type = context['type'], Accessories = context['accessories'], Material = context['material'], Finish = context['finish'],Price = cal, Location = context['location'], date = datetime.today()),
        # 'Jaunpur' : City10(Phone = details, Shape = context['shape'], Size = size, Loft = context['loft'], Type = context['type'], Accessories = context['accessories'], Material = context['material'], Finish = context['finish'],Price = cal, Location = context['location'], date = datetime.today())
    }
    city_obj = city[request.session.get('location')]
    city_obj.kitchen = details
    city_obj.save()

    context['size'] = size
    context['price'] = cal
    context['loft'] = request.session.get('loft') + ' feet loft'
    date = datetime.now().date()
    # Pdf generating script
    pdf = FPDF()
    pdf.add_page()
    pdf.image("static/pdf/bg_1.png", 0, 0, 210, 297, 'png')  # Background image
    pdf.image("static/pdf/Group.png", 100, 10)  # logo
    pdf.set_text_color(0, 102, 101)
    pdf.set_font("Arial", size=20)
    pdf.cell(190, 40, "Kitchendotcom", ln=1, align="C")

    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 8, "Name : ", ln=0, align="L")
    pdf.cell(20, 8, context['name'], ln=1, align="L")
    pdf.cell(40, 8, "Address : ", ln=0, align="L")
    pdf.cell(20, 8, context['location'], ln=1, align="L")
    pdf.cell(40, 8, "Contact No. : ", ln=0, align="L")
    pdf.cell(20, 8, request.session.get('phone'), ln=1, align="L")

    pdf.multi_cell(0, 10, "", align="L")

    pdf.set_fill_color(255, 255, 255)
    pdf.cell(190, 10, ln=1, border="L"+"T"+"R", fill=1)
    pdf.cell(190, 10, " Kitchendotcom", ln=1, border="L"+"R", align="L")
    pdf.cell(40, 10, " Address : ", ln=0, border="L", align="L", fill=1)
    pdf.cell(150, 10, "D65/245 Lahartara , Varanasi",
             ln=1, border="R", align="L", fill=1)
    pdf.cell(40, 10, " Date : ", ln=0, border="L"+"B", align="L")
    pdf.cell(150, 10, str(date), ln=1, border="B"+"R", align="L")

    pdf.set_font("Arial", size=15)
    pdf.cell(190, 20, "Quotation", ln=1, align="C")

    pdf.set_font("Arial", size=10)
    pdf.cell(30, 15, "Sr.No.", ln=0, border="L"+"T", align="C", fill=1)
    pdf.cell(40, 15, "Particulars", ln=0, border="T", align="L", fill=1)
    pdf.cell(40, 15, "Rate", ln=0, border="T", align="L", fill=1)
    pdf.cell(40, 15, "Sqft.", ln=0, border="T", align="L", fill=1)
    pdf.cell(40, 15, "Amount", ln=1, border="T"+"R", align="L", fill=1)
    pdf.cell(30, 10, "1.", ln=0, border="L", align="C", fill=1)
    pdf.cell(40, 10, "Plan Deisgning", ln=0, border="", align="L", fill=1)
    pdf.cell(40, 10, str(3*pdf_variable), ln=0, border="", align="L", fill=1)
    pdf.cell(40, 10, str(a+b+c), ln=0, border="", align="L", fill=1)
    pdf.cell(40, 10, str(round((a+b+c)*(3*pdf_variable), 2)),
             ln=1, border="R", align="L", fill=1)
    # pdf.set_fill_color(0,102,101)
    pdf.cell(30, 10, "2.", ln=0, border="L", align="C")
    pdf.cell(40, 10, "Loft", ln=0, border="", align="L")
    pdf.cell(40, 10, str(l*pdf_variable), ln=0, border="", align="L")
    pdf.cell(40, 10, str(a+b+c), ln=0, border="", align="L")
    pdf.cell(40, 10, str(round((a+b+c)*(l*pdf_variable), 2)),
             ln=1, border="R", align="L")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(190, 10, "", ln=1, border="L"+"R", align="C", fill=1)
    # pdf.set_fill_color(0,102,101)
    pdf.cell(190, 10, "", ln=1, border="L"+"R", align="C")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(10, 20, "", ln=0, border="L"+"B", fill=1)
    pdf.cell(140, 20, "Total", ln=0, border="B", align="L", fill=1)
    pdf.cell(40, 20, str(cal), ln=1, border="B"+"R", align="L", fill=1)

    pdf.multi_cell(0, 5, "", align="L")
    pdf.cell(200, 6, "Terms & Conditions :-", ln=1, align="L")
    pdf.set_font("Arial", size=8)
    pdf.cell(
        200, 4, "1. Above quotation is just for noted job works/Materials.", ln=1, align="L")
    pdf.cell(
        200, 4, "2. Payment is expected Either in Cash or Account transfer", ln=1, align="L")
    pdf.cell(200, 4, "3. No hidden costs further of any kind of expenses likeDesigning, transportation or installation,etc in case of turnkey.", ln=1, align="L")
    pdf.cell(200, 4, "4. Offers/schemes are marked as*For Free*.", ln=1, align="L")
    pdf.cell(200, 4, "5. Appliances and Services(Ceiling light, Civil work,Plumbing and Flooring) are not counted in above quotaion i.e. it will be quoted as per selection", ln=1, align="L")
    # pdf.cell(200,4,"6. Ceiling light, Civil work,Plumbing and Flooring not included . ", ln=1, align="L")
    pdf.cell(
        200, 4, "6. Payment Schedule as prescribed by area manager.", ln=1, align="L")

    pdf.add_page()
    pdf.image("static/pdf/bg_2.png", 0, 0, 210, 297, 'png')
    pdf.set_font("Arial", size=15)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(190, 15, "Summary", ln=1, align="C")

    pdf.set_font("Arial", size=10)
    pdf.cell(10, 15, "", ln=0, border="L"+"T", fill=1)
    pdf.cell(50, 15, "Sr.No.", ln=0, border="T", align="L", fill=1)
    pdf.cell(130, 15, "Particulars", ln=1, border="T"+"R", align="L", fill=1)
    pdf.cell(30, 10, "1.", ln=0, border="L", align="C", fill=1)
    pdf.cell(80, 10, "Shape", ln=0, border="", align="C", fill=1)
    pdf.cell(80, 10, context['shape'], ln=1, border="R", align="C", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.cell(30, 10, "2.", ln=0, border="L", align="C")
    pdf.cell(80, 10, "Size", ln=0, border="", align="C")
    pdf.cell(80, 10, str(a+b+c), ln=1, border="R", align="C")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(30, 10, "3.", ln=0, border="L", align="C", fill=1)
    pdf.cell(80, 10, "Type", ln=0, border="", align="C", fill=1)
    pdf.cell(80, 10, context['type'], ln=1, border="R", align="C", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.cell(30, 10, "4.", ln=0, border="L", align="C")
    pdf.cell(80, 10, "Material", ln=0, border="", align="C")
    pdf.cell(80, 10, context['material'], ln=1, border="R", align="C")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(30, 10, "5.", ln=0, border="L", align="C", fill=1)
    pdf.cell(80, 10, "Countertop", ln=0, border="", align="C", fill=1)
    pdf.cell(80, 10, context['countertop'],
             ln=1, border="R", align="C", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.cell(30, 10, "6.", ln=0, border="L", align="C")
    pdf.cell(80, 10, "Loft", ln=0, border="", align="C")
    pdf.cell(80, 10, context['loft'], ln=1, border="R", align="C")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(30, 10, "7.", ln=0, border="L", align="C", fill=1)
    pdf.cell(80, 10, "Finish", ln=0, border="", align="C", fill=1)
    pdf.cell(80, 10, context['finish'], ln=1, border="R", align="C", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.cell(30, 10, "8.", ln=0, border="L", align="C")
    pdf.cell(80, 10, "Accessories", ln=0, border="", align="C")
    pdf.cell(80, 10, context['accessories'], ln=1, border="R", align="C")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(20, 20, "Total", ln=0, border="L"+"B", align="R", fill=1)
    pdf.cell(135, 20, str(cal), ln=0, border="B", align="R", fill=1)
    pdf.cell(35, 20, "", ln=1, border="B"+"R", align="C", fill=1)

    pdf.set_font("Arial", size=15)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(190, 20, "Payment Schedule", ln=1, align="C")
    pdf.set_font("Arial", size=10)
    pdf.cell(35, 15, "  Sr.No.", ln=0, border="L"+"T", align="L", fill=1)
    pdf.cell(35, 15, "Date/Day", ln=0, border="T", align="L", fill=1)
    pdf.cell(35, 15, "Paid By", ln=0, border="T", align="L", fill=1)
    pdf.cell(35, 15, "Amount", ln=0, border="T", align="L", fill=1)
    pdf.cell(50, 15, "Mode of Payment", ln=1,
             border="T"+"R", align="L", fill=1)
    pdf.multi_cell(190, 10, "   1.", border="L"+"R", fill=1)
    pdf.set_fill_color(0, 102, 101)
    pdf.multi_cell(190, 10, "   2.", border="L"+"R")
    pdf.set_fill_color(255, 255, 255)
    pdf.multi_cell(190, 10, "   3.", border="L"+"R", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.multi_cell(190, 10, "   4.", border="L"+"R")
    pdf.set_fill_color(255, 255, 255)
    pdf.multi_cell(190, 10, "   5.", border="L"+"R", fill=1)
    # pdf.set_fill_color(0, 102, 101)
    pdf.multi_cell(190, 10, "   6.", border="L"+"R")
    pdf.set_fill_color(255, 255, 255)
    pdf.multi_cell(190, 10, "   7.", border="L"+"R", fill=1)
    # pdf.set_fill_color(0, 132, 153)
    pdf.multi_cell(190, 10, "   8.", border="L"+"R")
    pdf.set_fill_color(255, 255, 255)
    pdf.cell(190, 10, ln=1, border="L"+"B"+"R", fill=1)
    # Rows
    pdf.set_text_color(128, 128, 128)
    pdf.cell(200, 10, "www.kitchendotcom", ln=0, align="C")
    file_name = "media/pdf/" + str(request.session.session_key)+".pdf"
    pdf.output(name=file_name)

    # os.remove(file_name)
    # Email api
    template = render_to_string('email_template.html', {
                                'name': request.session.get('name')})
    email = EmailMessage(
        'Modular Kitchen Estimate',
        template,
        settings.EMAIL_HOST_USER,
        [request.session.get('email')]
    )
    # name = request.session.get('name') + '_KichenEstimate.pdf'
    email.attach_file(file_name)
    email.fail_silently = True
    # email.send()

    return render(request, 'kitchen_summary_buildpkg.html', {'context': context})


def summary_download(request):

    file_name = "media/pdf/" + str(request.session.session_key)+".pdf"
    file = open(file_name, 'rb')

    return FileResponse(file)


def customer_form(request, slug):
    temp_link = get_object_or_404(TempLink, link=slug)
    # if(temp_link.date)
    date_diff = (datetime.now().date() - temp_link.date)
    if (date_diff.days > 2):
        temp_link.delete()
        return HttpResponse('<h1>link expired</h1>')

    order_instance = temp_link.kitchen_details

    if (request.method == 'POST'):
        data = KitchenDetailsForm(request.POST, instance=order_instance)
        imgs = KitchenImageFormSet(
            request.POST, request.FILES, instance=order_instance)

        if data.is_valid() and imgs.is_valid():
            # pass
            data.save()
            imgs.save()
            # stat = imgs.save()
            # print(stat)
        else:
            return HttpResponse('<h1>bad request</h1>')
        return HttpResponse('<h1>response recorded</h1>')

    form_instance = KitchenDetailsForm(instance=order_instance)
    imgformset_instance = KitchenImageFormSet(instance=order_instance)
    vidformset_instance = KitchenVideoFormSet(instance=order_instance)

    context = {
        'form_inst': form_instance,
        'imgformset_instance': imgformset_instance,
        'vidformset_instance': vidformset_instance,
    }
    return render(request, 'customer_form.html', context)

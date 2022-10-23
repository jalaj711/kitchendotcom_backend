from django.utils.html import format_html
from datetime import date, datetime, timedelta
from home.models import c_details, kitchen_details, Constant
from home.models import City1, City2, City3, City4, City5, City6, City7, City8, City9, City10, City11, City12, City13, Other
from home.models import TempLink, KitchenImage, KitchenVideo
from django.db import models
from django.contrib import admin


# Displaying Models
# class Kd_Admin(admin.ModelAdmin):
#     list_display = ["layout", "Shape", "Countertop", "loft"]


# class Cd_Admin(admin.ModelAdmin):
#     list_display = ["name", "phone", "email"]

# class Calc_Admin(admin.ModelAdmin):
#     list_display = ["a_feet", "a_inch", "b_feet", "b_inch", "c_feet", "c_inch"]


# Register your models here.
admin.site.register(c_details)
# admin.site.register(calculation)
admin.site.register(Constant)


@admin.action(description="Create temp links")
def create_link(modeladmin, request, queryset):
    for query in queryset:
        TempLink.objects.create(kitchen_details=query)


@admin.action(description="Create temp links")
def create_link_city(modeladmin, request, queryset):
    for query in queryset:
        TempLink.objects.create(kitchen_details=query.kitchen)


class KitchenImageInline(admin.StackedInline):
    model = KitchenImage
    extra = 0
    max_num = 5


class KitchenVideoInline(admin.StackedInline):
    model = KitchenVideo
    extra = 0
    max_num = 5


@admin.register(kitchen_details)
class kitchen_detailsAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Location', 'Price',
                    'getTempLink',  'link_expiry', 'invoice']
    # ordering = ['Date']

    def getTempLink(self, x):
        tempLinkObj = TempLink.objects.get(kitchen_details=x)
        linkBtn = "<div onClick=\"copyToClip(this)\" value=\"kitchendotcom.in/custormerform/{tmpLinkObj}\" class=\"button\">Copy</div>".format(
            tmpLinkObj=tempLinkObj.link)
        return format_html(linkBtn)

    def invoice(self, x):
        return format_html("<a target=\"_blank\" class=\"button\" href=\"/billing\">create</a>")

    def link_expiry(self, x):
        tempLinkObj = TempLink.objects.get(kitchen_details=x)
        if tempLinkObj.date:
            date_diff = (datetime.now().date() - tempLinkObj.date)
            if(date_diff.days > 2):
                return 'expired'
            else:
                return (tempLinkObj.date + timedelta(days=2))
        else:
            return '-'

    actions = [create_link]
    inlines = [KitchenImageInline, KitchenVideoInline]

    class Media:
        js = ("admin/copy-btn.js",)


class CitysAdmin(admin.ModelAdmin):
    list_display = ['Location', 'customer_name',
                    'kitchen_shape', 'kitchen_size', 'price', 'getTempLink', 'link_expiry', 'invoice']

    def Location(self, x):
        location = x.kitchen.Location
        return location

    def customer_name(self, x):
        cust_name = x.kitchen.Name
        link = "<a href=\"/admin/home/kitchen_details/{link}\">{link_name}</a>".format(
            link=x.kitchen.pk, link_name=cust_name)
        return format_html(link)

    def invoice(self, x):
        return format_html("<a class=\"button\" target=\"_blank\" href=\"/billing\">create</a>")

    def kitchen_shape(self, x):
        link = "<a href=\"/admin/home/kitchen_details/{link}\">{link_name}</a>".format(
            link=x.kitchen.pk, link_name=x.kitchen.Shape)
        return format_html(link)

    def kitchen_size(self, x):
        return x.kitchen.Size

    def price(self, x):
        return x.kitchen.Price

    def getTempLink(self, x):
        tempLinkObj = TempLink.objects.get(kitchen_details=x.kitchen)
        linkBtn = "<div onClick=\"copyToClip(this)\" value=\"kitchendotcom.in/custormerform/{tmpLinkObj}\" class=\"button\">Copy</div>".format(
            tmpLinkObj=tempLinkObj.link)
        return format_html(linkBtn)

    def link_expiry(self, x):
        tempLinkObj = TempLink.objects.get(kitchen_details=x.kitchen)
        if tempLinkObj.date:
            date_diff = (datetime.now().date() - tempLinkObj.date)
            if(date_diff.days > 2):
                return 'expired'
            else:
                return (tempLinkObj.date + timedelta(days=2))
        else:
            return '-'

    # def kitchen_images(self,x):
        # return x.kitchen.image

    actions = [create_link_city]

    class Media:
        js = ("admin/copy-btn.js",)


admin.site.register(City1, CitysAdmin)
admin.site.register(City2, CitysAdmin)
admin.site.register(City3, CitysAdmin)
admin.site.register(City4, CitysAdmin)
admin.site.register(City5, CitysAdmin)
admin.site.register(City6, CitysAdmin)
admin.site.register(City7, CitysAdmin)
admin.site.register(City8, CitysAdmin)
admin.site.register(City9, CitysAdmin)
admin.site.register(City10, CitysAdmin)
admin.site.register(City11, CitysAdmin)
admin.site.register(City12, CitysAdmin)
admin.site.register(City13, CitysAdmin)
admin.site.register(Other, CitysAdmin)
# admin.site.register(KitchenImage)
# admin.site.register(KitchenVid)


@admin.register(TempLink)
class TempLinkAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'getTempLink', 'expiry_date']

    def getTempLink(self, x):
        return x.link

    def expiry_date(self, x):
        return (x.date + timedelta(days=2))

    class Media:
        js = ("admin/copy-btn.js",)

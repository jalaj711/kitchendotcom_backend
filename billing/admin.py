from django.contrib import admin
from .models import Bill, Bill_Item


# admin.site.register(Bill)
admin.site.register(Bill_Item)


class BillItemInline(admin.StackedInline):
    model = Bill_Item
    extra = 0


@admin.register(Bill)
class Bill_admin(admin.ModelAdmin):
    inlines = [BillItemInline]

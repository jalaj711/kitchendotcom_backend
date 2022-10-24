"""Kitchendotcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from home import views

urlpatterns = [
    path("", views.landing_page, name='home'),
    path("contactus/", views.contact_us, name="contact_us"),
    path("aboutus/", views.about_us, name="about_us"),
    # path("project_gallery", views.project_gallery, name='project_gallery'),
    path("design_gallery", views.design_gallery, name='design_gallery'),
    path("kitchen_price_steps", views.kitchen_price_steps,
         name='kitchen_price_steps'),
    path("select-layout/", views.select_layout, name='select_layout'),
    path("customer-details", views.customer_details, name='customer_details'),
    path("select-dimension", views.layout_dimensions, name='select_lshape'),
    path("select_countertop", views.select_countertop, name='select_countertop'),
    path("select_loft_type", views.select_loft_type,
         name='select_loft_type'),  # might be changed
    path("select_package", views.select_package, name='select_package'),
    path("select_package/premium", views.select_package_premium,
         name='select_package_premium'),
    path("select_package/luxe", views.select_package_luxe,
         name='select_package_luxe'),
    path("select_package/essentials", views.select_package_essentials,
         name='select_package_essentials'),
    path("select_package/buildpackage", views.select_package_buildpkg,
         name='select_package_buildpkg'),
    path("build_package", views.build_package, name='build_package'),
    path("build_package/hdhmr", views.build_package_hdhmr,
         name='build_package_hdhmr'),
    path("build_package/mrplywood", views.build_package_mrply,
         name='build_package_mrply'),
    path("build_package/bwrplywood", views.build_package_bwrply,
         name='build_package_bwrply'),
    path("build_package/bwpplywood", views.build_package_bwpply,
         name='build_package_bwpply'),
    path("select_finish", views.select_finish, name='select_finish'),
    path("select_finish/laminate", views.select_finish_laminate,
         name='select_finish_laminate'),
    path("select_finish/pvclaminate", views.select_finish_pvclaminate,
         name='select_finish_pvclaminate'),
    path("select_finish/asacrylic", views.select_finish_asacrylic,
         name='select_finish_asacrylic'),
    path("select_finish/glossypu", views.select_finish_glossypu,
         name='select_finish_glossypu'),
    path("select_accessories", views.select_accessories, name='select_accessories'),
    path("select_accessories/basic", views.select_accessories_basic,
         name='select_accessories_basic'),
    path("select_accessories/intermediate", views.select_accessories_intermediate,
         name='select_accessories_intermediate'),
    path("select_accessories/premium", views.select_accessories_premium,
         name='select_accessories_premium'),
    path("select_appliances", views.select_appliances, name='select_appliances'),
    path("select_services", views.select_services, name='select_services'),
    path("summary", views.kitchen_summary, name='kitchen_summary'),
    path("summary_download", views.summary_download, name='summary_download'),
    path("summary/buildpkg", views.kitchen_summary_buildpkg,
         name='kitchen_summary_buildpkg'),
    path("custormerform/<str:slug>", views.customer_form, name='customer_form'),
]

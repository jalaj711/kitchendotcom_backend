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
    path("contact-us/", views.contact_us, name="contact_us"),
    path("aboutus/", views.about_us, name="about_us"),
    # path("project_gallery", views.project_gallery, name='project_gallery'),
    path("design_gallery", views.design_gallery, name='design_gallery'),
    path("kitchen_price_steps", views.kitchen_price_steps,
         name='kitchen_price_steps'),
    path("select-layout/", views.select_layout, name='select_layout'),
    path("customer-details/", views.customer_details, name='customer_details'),
    path("select-dimension/", views.layout_dimensions, name='select_lshape'),
    path("select-countertop/", views.select_countertop, name='select_countertop'),
    path("select-loft-type/", views.select_loft_type,
         name='select_loft_type'),  # might be changed
    path("select-package/", views.select_package, name='select_package'),
    path("build-package/", views.build_package, name='build_package'),
    path("select-finish/", views.select_finish, name='select_finish'),
    path("select-accessories/", views.select_accessories, name='select_accessories'),
    path("select-appliances/", views.select_appliances, name='select_appliances'),
    path("select-services/", views.select_services, name='select_services'),
    path("summary", views.kitchen_summary, name='kitchen_summary'),
    path("summary_download", views.summary_download, name='summary_download'),
    path("summary/buildpkg", views.kitchen_summary_buildpkg,
         name='kitchen_summary_buildpkg'),
    path("custormerform/<str:slug>", views.customer_form, name='customer_form'),
]

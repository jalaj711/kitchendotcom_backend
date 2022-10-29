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
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("contact-us", views.contact_us, name="contact_us"),
    path("about-us", views.about_us, name="about_us"),
    path("project-gallery", views.project_gallery, name="project_gallery"),
    path("design-gallery", views.design_gallery, name="design_gallery"),
    path("blog", views.blog, name="blog"),
    path("estimator", views.estimator, name="estimator"),
    path("estimator/select-layout", views.estimator_select_layout,
         name="estimator_select_layout"),
    path("estimator/customer-details", views.estimator_customer_details,
         name="estimator_customer_details"),
    path("estimator/select-dimensions/l-shape", views.estimator_select_dimensions_l_shape,
         name="estimator_select_dimensions_l_shape"),
    path("estimator/select-dimensions/straight-shape", views.estimator_select_dimensions_straight_shape,
         name="estimator_select_dimensions_straight_shape"),
    path("estimator/select-dimensions/u-shape", views.estimator_select_dimensions_u_shape,
         name="estimator_select_dimensions_u_shape"),
    path("estimator/select-dimensions/parallel-shape", views.estimator_select_dimensions_parallel_shape,
         name="estimator_select_dimensions_parallel_shape"),
    path("estimator/select-loft-type", views.estimator_select_loft_type,
         name="estimator_select_loft_type"),
    path("estimator/select-package", views.estimator_select_package,
         name="estimator_select_package"),
    path("estimator/select-package/essentials", views.estimator_select_package_essentials,
         name="estimator_select_package_essentials"),
    path("estimator/select-package/premium", views.estimator_select_package_premium,
         name="estimator_select_package_premium"),
    path("estimator/select-package/luxe", views.estimator_select_package_luxe,
         name="estimator_select_package_luxe"),
    path("estimator/select-package/build-your-own", views.estimator_select_package_build_your_own,
         name="estimator_select_package_build_your_own"),
    path("estimator/build-package", views.estimator_build_package,
         name="estimator_build_package"),
    path("estimator/build-package/hdhmr", views.estimator_build_package_hdhmr,
         name="estimator_build_package_hdhmr"),
    path("estimator/build-package/mr-plywood", views.estimator_build_package_mr_plywood,
         name="estimator_build_package_mr_plywood"),
    path("estimator/build-package/bwr-plywood", views.estimator_build_package_bwr_plywood,
         name="estimator_build_package_bwr_plywood"),
    path("estimator/build-package/bwp-plywood", views.estimator_build_package_bwp_plywood,
         name="estimator_build_package_bwp_plywood"),
    path("estimator/select-countertop", views.estimator_select_countertop,
         name="estimator_select_countertop"),
    path("estimator/select-finish", views.estimator_select_finish,
         name="estimator_select_finish"),
    path("estimator/select-finish/laminate", views.estimator_select_finish_laminate,
         name="estimator_select_finish_laminate"),
    path("estimator/select-finish/pvc-laminate", views.estimator_select_finish_pvc_laminate,
         name="estimator_select_finish_pvc_laminate"),
    path("estimator/select-finish/anti-scratch-acrylic", views.estimator_select_finish_anti_scratch_acrylic,
         name="estimator_select_finish_anti_scratch_acrylic"),
    path("estimator/select-finish/glossy-pu", views.estimator_select_finish_glossy_pu,
         name="estimator_select_finish_glossy_pu"),
    path("estimator/select-accessories", views.estimator_select_accessories,
         name="estimator_select_accessories"),
    path("estimator/select-accessories/basic", views.estimator_select_accessories_basic,
         name="estimator_select_accessories_basic"),
    path("estimator/select-accessories/intermediate", views.estimator_select_accessories_intermediate,
         name="estimator_select_accessories_intermediate"),
    path("estimator/select-accessories/premium", views.estimator_select_accessories_premium,
         name="estimator_select_accessories_premium"),
    path("estimator/select-services", views.estimator_select_services,
         name="estimator_select_services"),
    path("estimator/select-appliances", views.estimator_select_appliances,
         name="estimator_select_appliances"),
    path("estimator/summary", views.estimator_summary,
         name="estimator_summary"),
]

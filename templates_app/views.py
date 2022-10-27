from django.shortcuts import render

# Create your views here..html")


def landing_page(request):
    return render(request, "index.html")


def contact_us(request):
    return render(request, "contact-us.html")


def about_us(request):
    return render(request, "about-us.html")


def project_gallery(request):
    return render(request, "project-gallery.html")


def design_gallery(request):
    return render(request, "design-gallery.html")


def estimator(request):
    return render(request, "estimator.html")


def estimator_select_layout(request):
    return render(request, "estimator/select-layout.html")


def estimator_customer_details(request):
    return render(request, "estimator/customer-details.html")


def estimator_select_dimensions_l_shape(request):
    return render(request, "estimator/select-dimensions/l-shape.html")


def estimator_select_dimensions_straight_shape(request):
    return render(request, "estimator/select-dimensions/straight-shape.html")


def estimator_select_dimensions_u_shape(request):
    return render(request, "estimator/select-dimensions/u-shape.html")


def estimator_select_dimensions_parallel_shape(request):
    return render(request, "estimator/select-dimensions/parallel-shape.html")


def estimator_select_loft_type(request):
    return render(request, "estimator/select-loft-type.html")


def estimator_select_package(request):
    return render(request, "estimator/select-package.html")


def estimator_select_package_essentials(request):
    return render(request, "estimator/select-packageessentials.html")


def estimator_select_package_premium(request):
    return render(request, "estimator/select-package/premium.html")


def estimator_select_package_luxe(request):
    return render(request, "estimator/select-package/luxe.html")


def estimator_select_package_build_your_own(request):
    return render(request, "estimator/select-package/build-your-own.html")


def estimator_build_package(request):
    return render(request, "estimator/build-package.html")


def estimator_build_package_hdhmr(request):
    return render(request, "estimator/build-package/hdhmr.html")


def estimator_build_package_mr_plywood(request):
    return render(request, "estimator/build-package/mr-plywood.html")


def estimator_build_package_bwr_plywood(request):
    return render(request, "estimator/build-package/bwr-plywood.html")


def estimator_build_package_bwp_plywood(request):
    return render(request, "estimator/build-package/bwp-plywood.html")


def estimator_select_countertop(request):
    return render(request, "estimator/select-countertop.html")


def estimator_select_finish(request):
    return render(request, "estimator/select-finish.html")


def estimator_select_finish_laminate(request):
    return render(request, "estimator/select-finish/laminate.html")


def estimator_select_finish_pvc_laminate(request):
    return render(request, "estimator/select-finish/pvc-laminate.html")


def estimator_select_finish_anti_scratch_acrylic(request):
    return render(request, "estimator/select-finish/anti-scratch-acrylic.html")


def estimator_select_finish_glossy_pu(request):
    return render(request, "estimator/select-finish/glossy-pu.html")


def estimator_select_accessories(request):
    return render(request, "estimator/select-accessories.html")


def estimator_select_accessories_basic(request):
    return render(request, "estimator/select-accessories/basic.html")


def estimator_select_accessories_intermediate(request):
    return render(request, "estimator/select-accessories/intermediate.html")


def estimator_select_accessories_premium(request):
    return render(request, "estimator/select-accessories/premium.html")


def estimator_select_services(request):
    return render(request, "estimator/select-services.html")


def estimator_select_appliances(request):
    return render(request, "estimator/select-appliances.html")

def estimator_summary(request):
    return render(request, "estimator/summary.html")
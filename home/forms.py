from django.forms import ModelForm, inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row
from django import forms

from home.models import kitchen_details, KitchenImage, KitchenVideo

# TODO
# model countertop boolean
# model appliances size 132

SHAPE_CHOICES = [
    ('L', 'L-Shaped Design '),
    ('U', 'U-Shaped Design '),
    ('Straight', 'Straight Shaped Design'),
    ('Parallel', 'Parallel Shaped Design')
]

MATERIAL_CHOICES = [
    ('HDHMR', 'HDHMR'),
    ('MR Plywood', 'MR Plywood'),
    ('BWR Plywood', 'BWR Plywood '),
    ('BWP Plywood', 'BWP Plywood '),
]

BOOL_CHOICES = [
    ('YES', 'yes'),
    ('NO', 'No')
]

LOFT_CHOICES = [
    ('0', 'No loft'),
    ('1', '1 feet loft'),
    ('2', '2 feet loft'),
    ('3', '3 feet loft'),
    ('4', '4 feet loft'),
    ('5', '5 feet loft'),
    ('6', '6 feet loft'),
    ('7', '7 feet loft'),
    ('8', '8 feet loft'),
    ('9', '9 feet loft'),
    ('10', '10 feet loft'),
]

FINISH_CHOICES = [
    ('Laminate', 'Laminate'),
    ('PVC Laminate', 'PVC Laminate'),
    ('Anti-scratch Acrylic', 'Anti-scratch Acrylic'),
    ('Glossy PU', 'Glossy PU')
]

ACCESSORIES_CHOICES = [
    ('Basic', 'Basic'),
    ('Intermediate', 'Intermediate'),
    ('Premium', 'Premium')
]

SERVICES_CHOICES = [
    ('Painting', 'Painting'),
    ('Plumbing', 'Plumbing'),
    ('Electrical', 'Electrical'),
    ('Platform', 'Platform'),
    ('Dado', 'Dado')
]

APPLLIANCES_CHOICES = [
    ('Hob', 'Hob'),
    ('Chimney', 'Chimney'),
    ('Faucets & Sink', 'Faucets & Sink'),
    ('Built In Microwave', 'Built In Microwave'),
    ('Built In Oven', 'Built In Oven'),
    ('Refrigerator', 'Refrigerator'),
]


KitchenImageFormSet = inlineformset_factory(
    kitchen_details, KitchenImage, fields=('image',), extra=5, max_num=5, )

KitchenVideoFormSet = inlineformset_factory(
    kitchen_details, KitchenVideo, fields=('video',), extra=5, max_num=5)


class KitchenDetailsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(KitchenDetailsForm, self).__init__(*args, **kwargs)

    # If you pass FormHelper constructor a form instance
    # It builds a default layout with all its fields
        self.helper = FormHelper(self)

    # You can dynamically adjust your layout
        self.helper.layout = Layout(
            Row('Name'),
            Row('Shape', 'Size'),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )

    class Meta:
        model = kitchen_details
        # exclude = ['Price', 'Location', 'date']
        exclude = ['Status']
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'readonly': True}),
            'Type': forms.TextInput(attrs={'readonly': True}),
            'Price': forms.TextInput(attrs={'readonly': True}),
            'Location': forms.TextInput(attrs={'readonly': True}),
            'date': forms.TextInput(attrs={'readonly': True}),
            'Shape': forms.Select(choices=SHAPE_CHOICES),
            'Material': forms.RadioSelect(choices=MATERIAL_CHOICES),
            'Loft': forms.Select(choices=LOFT_CHOICES),
            'Finish': forms.RadioSelect(choices=FINISH_CHOICES),
            'Accessories': forms.RadioSelect(choices=ACCESSORIES_CHOICES),
            # 'Services': forms.CheckboxSelectMultiple(choices=SERVICES_CHOICES),
            # 'Appliances': forms.CheckboxSelectMultiple(
            #     choices=APPLLIANCES_CHOICES),
        }

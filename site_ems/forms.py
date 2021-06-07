from django import forms
from .models import Company,Location,Area,Smartmeter,SmartmeterPort,Brand_and_Manufacturer,Costarea
from .models import Consumer,House

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_id','short_name','company_name1','company_name2','street','town','zip_code',
                  'country','contact_person','tel_no','company_url','email','fax_no','tax_no1','tax_no2',
                  'company_logo']

        widget = {
            'country': forms.TextInput(attrs={'class': 'form-control'})
        }

class LocationForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(),initial=0,required=False)
    class Meta:
        model = Location
        fields = ['company','short_name','description','street','town','zip_code','country','contact_person',
                  'email','tel_no','fax_no','location_logo']
        widget = {
            'country': forms.TextInput(attrs={'class': 'form-control'})
        }

class AreaForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(),initial=0,required=False)
    location = forms.ModelChoiceField(queryset=Location.objects.all(),initial=0,required=False)

    class Meta:
        model = Area
        fields =['company','location','area','area_logo']

class CostareaForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), initial=0, required=False)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), initial=0, required=False)

    class Meta:
        model = Costarea
        fields = ['company', 'location', 'cost_area']

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
class HouseForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), initial=0, required=False)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), initial=0, required=False)
    tax_marker = forms.ChoiceField(choices=BOOL_CHOICES,widget=forms.RadioSelect())

    class Meta:
        model = House
        fields = ['company', 'location', 'costarea_id','house_name','street1','street2','city',
                  'zipcode','state','country','provider','floors_start_from','floors_end_to','remarks','tax_marker']

class ConsumerForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), initial=0, required=False)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), initial=0, required=False)

    class Meta:
        model = Consumer
        fields = ['consumer_name','company', 'location', 'area','house','floor_no']

class SmartmeterForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), initial=0)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), initial=0)
    area = forms.ModelChoiceField(queryset=Area.objects.all(),initial=0)
    class Meta:
        model = Smartmeter
        fields = ['brand_id','description','max_no_of_channels']

class SmartmeterPortForm(forms.ModelForm):
    class Meta:
        model = SmartmeterPort
        fields = ['port_type','communication_type','reading_type','baud_rate','data_bits','parity',
                  'stop_bits','flow_control']

class SmartmeterLinkDeviceForm(forms.Form):
    device_name = forms.CharField(max_length=20)
    port_type = forms.ChoiceField()
    link_name = forms.CharField(max_length=40)
    communication_type = forms.ChoiceField()

class BrandandManufacturerForm(forms.ModelForm):
    class Meta:
        model = Brand_and_Manufacturer
        fields = ['brand_name','brand_model','brand_type','manufacturer','description','max_no_of_channels']
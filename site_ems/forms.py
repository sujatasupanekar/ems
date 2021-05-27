from django import forms
from .models import Company,Location,Area,Smartmeter,SmartmeterPort,Brand_and_Manufacturer

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
    company = forms.ModelChoiceField(queryset=Company.objects.all(),initial=0)

    class Meta:
        model = Location
        fields = ['company','short_name','description','street','town','zip_code','country','contact_person',
                  'email','tel_no','fax_no','location_logo']

        widget = {
            'country': forms.TextInput(attrs={'class': 'form-control'})
        }


class AreaForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(),initial=0)
    location = forms.ModelChoiceField(queryset=Location.objects.all(),initial=0)

    class Meta:
        model = Area
        fields =['company','location','area','area_logo']

class SmartmeterForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), initial=0)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), initial=0)

    class Meta:
        model = Smartmeter
        fields = ['brand_id','description','max_no_of_channels']

class SmartmeterPortForm(forms.ModelForm):
    class Meta:
        model = SmartmeterPort
        fields = ['port_type','communication_type','reading_type','baud_rate','data_bits','parity',
                  'stop_bits','flow_control']

class BrandandManufacturerForm(forms.ModelForm):
    class Meta:
        model = Brand_and_Manufacturer
        fields = ['brand_name','brand_model','brand_type','manufacturer','description','max_no_of_channels']
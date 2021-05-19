from django import forms
from .models import Company,Location,Area

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
    company = forms.ModelChoiceField(queryset=Company.objects.values_list('company_name1',flat=True),initial=0)

    class Meta:
        model = Location
        fields = ['company','short_name','description','street','town','zip_code','country','contact_person',
                  'email','tel_no','fax_no','location_logo']

        widget = {
            'country': forms.TextInput(attrs={'class': 'form-control'})
        }


class AreaForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.values_list('company_name1',flat=True),initial=0)
    location = forms.ModelChoiceField(queryset=Location.objects.values_list('short_name',flat=True),initial=0)
    class Meta:
        model = Area
        fields =['company','location','area','area_logo']
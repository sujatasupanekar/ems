from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import views as auth_views, get_user_model
from django import forms
from django.views.generic import FormView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from .models import Company,Location,Consortium,Area,Smartmeter,SmartmeterPort,Brand_and_Manufacturer
from .forms import CompanyForm,LocationForm,AreaForm,SmartmeterForm,SmartmeterPortForm,BrandandManufacturerForm
import random

# Create your views here.
def index(request):
    print("in index ")
    return HttpResponse('Hello, welcome to the index page.')

def consumption_graph(request):
    randomlist = []
    for i in range(0, 50):
        n = random.randint(1000, 9999)
        randomlist.append(n)
    print(randomlist)
    return render(request,'consumption_graph.html',{'data_set':randomlist})

def addsmartmeter(request):
    if request.method == "POST":
        form = SmartmeterForm(request.POST)
        if form.is_valid():
                Smartmeter = form.save(commit=False)
                Smartmeter.createdby = request.user
                Smartmeter.modifiedby = request.user
                Smartmeter = Smartmeter.save()
                print(" form is valid and in try block")
                return redirect('/showsmartmeter')
    else:
        print("in else part")
        form = SmartmeterForm()
    return render(request,'addsmartmeter.html',{'form':form})

def showsmartmeter(request):
    result = Smartmeter.objects.all()
    return render(request, 'showsmartmeter.html', {'result': result})

def smartmeterport(request):
    form = SmartmeterPortForm()
    if request.method == "POST":
        form = SmartmeterPortForm(request.POST)
        if form.is_valid():
                SmartmeterPort = form.save(commit=False)
                SmartmeterPort.createdby = request.user
                SmartmeterPort.modifiedby = request.user
                SmartmeterPort = SmartmeterPort.save()
                print(" form is valid and in try block")
                return redirect('/showsmartmeter')
    else:
        print("in else part")
        form = SmartmeterPortForm()
    return render(request,"smartmeterport.html",{'form':form})

def editsmartmeter(request, id):
    obj = Location.objects.get(location_id=id)
    updated_on = obj.modifieddate
    return render(request, 'editlocation.html', {'employee': obj, 'updated_on': updated_on})

def brandandmanuf(request):
    form = BrandandManufacturerForm()
    if request.method == "POST":
        form = BrandandManufacturerForm(request.POST)
        if form.is_valid():
            Brand_and_Manufacturer = form.save(commit=False)
            Brand_and_Manufacturer.createdby = request.user
            Brand_and_Manufacturer.modifiedby = request.user
            Brand_and_Manufacturer = Brand_and_Manufacturer.save()
            print(" form is valid and in try block")
            return redirect('/showbrandandmanuf')
    else:
        print("in else part")
        form = BrandandManufacturerForm()
    return render(request, "brandandmanuf.html", {'form': form})

def showbrandandmanuf(request):
    cd = Brand_and_Manufacturer.objects.all()
    return render(request, "showbrandandmanuf.html", {'result': cd})


def about(request):
    return render(request, 'about.html')

def home(request):
    if request.user.is_superuser:
        return render(request, 'adminpage.html')
    else:
        return render(request,'userpage.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        unm = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=unm, password=password)

        if user is not None:
            auth.login(request, user)
            if request.user.is_superuser:
                return render(request, 'adminpage.html')
            else:
                return render(request, 'userpage.html')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login_page')
    else:
        return render(request, 'login_page.html')

def adminpage(request):
    return render(request, 'adminpage.html')

def userpage(request):
    return render(request, 'userpage.html')

def addcompany(request):
    #full_list = get_consortium()
    #print(full_list)
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
                Company = form.save(commit=False)
                Company.createdby = request.user
                Company.modifiedby = request.user
                Company= Company.save()
                print(" form is valid and in try block")
                return redirect('/showcompany')
    else:
        print("in else part")
        form = CompanyForm()
    return render(request,'addcompany.html',{'form':form})

def showcompany(request):
    cd = Company.objects.all()
   # for i in cd:
   #     instance = i.createddate
   #     print(instance)
    return render(request, "showcompany.html", {'cd': cd})

def editcompany(request, id):
    employee = Company.objects.get(company_id=id)
    updated_on = employee.modifieddate
    return render(request,'editcompany.html', {'employee':employee,'updated_on':updated_on})

def updatecompany(request, id):
    form = CompanyForm()
    if request.method == 'POST':
        employee = Company.objects.get(company_id=id)
        form = CompanyForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            print("in update inside loop:", employee)
            return redirect("/showcompany")
    return render(request, 'editcompany.html', {'employee': employee})

def destroycompany(request, id):
    print("company id",id)
    employee = Company.objects.get(company_id=id)
    employee.delete()
    return redirect("/showcompany")

def get_company_list():
    cmp_list = []
    t1 = Company.objects.all()
    for i in t1:
        cmp_list.append(i.company_name1)
    return cmp_list

def get_consortium():
    temp = Consortium.objects.all()
    ls = []
    for i in temp:
        temp1 = i.consortium_name1
        ls.append(temp1)

    print("ls:",ls)
    return ls

def addlocation(request):
    if request.method == "POST":
        form = LocationForm(request.POST or None)
        if form.is_valid():
                location = form.save(commit=False)
                location.createdby = request.user
                location.modifiedby = request.user
                print(location)
                location.save()
                print(" form is valid and in try block")
                return redirect('/showlocation')
    else:
        print("in else part")
        form = LocationForm()
    return render(request,'addlocation.html',{'form':form})

def showlocation(request):
    result = Location.objects.all()
    #print(result)
    return render(request,'showlocation.html',{'result':result})

def editlocation(request, id):
    obj = Location.objects.get(location_id=id)
    updated_on = obj.modifieddate
    print("obj in Edit location:",obj,id)
    cnm_list = Company.objects.all()
    return render(request,'editlocation.html', {'cnm_list':cnm_list,'employee':obj,'updated_on':updated_on})

def updatelocation(request, id):
    form = LocationForm()
    if request.method == 'POST':
        obj = Location.objects.get(location_id=id)
        print("obj in update location:",obj,id)
        form = LocationForm(request.POST, instance=obj)
        if form.is_valid():
            print("in form valid block")
            form.save()
            return redirect("/showlocation")
        else:
            print("Form errors: ",form.errors)
    return render(request, 'editlocation.html', {'employee': obj})

def destroylocation(request, id):
    print("location id",id)
    obj = Location.objects.get(location_id=id)
    obj.delete()
    return redirect("/showlocation")

def get_location_list():
    lnm_list = []
    t2 = Location.objects.all()
    for j in t2:
        lnm_list.append(j.short_name)
    return lnm_list

def addarea(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            Area = form.save(commit=False)
            Area.createdby = request.user
            Area.modifiedby = request.user
            Area = Area.save()
            print(" form is valid and in try block")
            return redirect('/showarea')
    else:
        print("in else part")
        form = AreaForm()
    return render(request, 'addarea.html', {'form': form})

def showarea(request):
    result = Area.objects.all()
    return render(request, 'showarea.html',{'result':result})

def load_location(request):
    company_id = request.GET.get('company_id')
    locations = Company.objects.filter(company_id=company_id).all()
    return render(request, 'location_dropdown.html', {'locations': locations})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def editarea(request, id):
    obj = Area.objects.get(area_id=id)
    print("obj:", obj)
    cnm_list = get_company_list()
    #cnm_list = Company.objects.all()
    lnm_list = Location.objects.all()
    updated_on = obj.modifieddate
    print("cnm_list:",cnm_list)
    return render(request,'editarea.html', {'cmp_list':cnm_list,'lnm_list':lnm_list,'employee':obj,'updated_on':updated_on})

def updatearea(request, id):
    form = AreaForm()
    if request.method == 'POST':
        obj = Area.objects.get(area_id=id)
        print("obj:",obj)
        form = AreaForm(request.POST, instance=obj)
        cnm_list = get_company_list()
        lnm_list = get_location_list()
        updated_on = obj.modifieddate
        if form.is_valid():
            form.save()
            print("in if form valid loop")
            return redirect("/showarea")
        else:
            print(form.errors)
    return render(request, 'editarea.html', {'cmp_list':cnm_list,'lnm_list':lnm_list,'employee': obj,'updated_on':updated_on})

def destroyarea(request, id):
    #print("company id",id)
    obj = Area.objects.get(area_id=id)
    obj.delete()
    return redirect("/showarea")



def roicalc(request):
    return render(request,'roicalc.html')


def error_404(request,exception):
    values_for_template = {}
    return render(request, 'page_not_found.html', values_for_template, status=404)

def error_500(request,exception):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request, 'server_error.html', values_for_template, status=500)

def server_error(request):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request,'server_error.html',values_for_template,status=500)

def error_403(request,exception):
    values_for_template = {}
    return render(request, 'permission_denied.html', values_for_template, status=403)

def error_400(request,exception):
    values_for_template = {}
    return render(request, 'bad_request.html', values_for_template, status=400)

def logout(request):
    auth.logout(request)
    return redirect('/')

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "Forgot_password/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'ecubesolutions.in',
                    'site_name': 'ecubesolutions.in',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'ecubesolutio99@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("/")
                    #return redirect ("/password_reset/done/")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request= request, template_name="Forgot_password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


class SetPasswordForm(forms.Form):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
        }
    new_password1 = forms.CharField(label=("New password"), required=True,
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=("New password confirmation"), required=True,
                                    widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

class PasswordResetConfirmView(FormView):
    template_name = "Forgot_password/password_reset_confirm.html"
    success_url = '/admin/'
    form_class = SetPasswordForm

    def form_valid(self, *arg, **kwargs):
        form = super(PasswordResetConfirmView, self).form_valid(*arg, **kwargs)
        uidb64=self.kwargs['uidb64']
        token=self.kwargs['token']
        UserModel = get_user_model()
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            new_password= form.cleaned_data['new_password2']
            user.set_password(new_password)
            user.save()
            messages.success(self.request, 'Password reset has been successful.')
        else:
            messages.error(self.request, 'Password reset has not been unsuccessful.')
        return form
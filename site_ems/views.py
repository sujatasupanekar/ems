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
from .models import Company,Location,Consortium,Area,Smartmeter,SmartmeterPort,Brand_and_Manufacturer,Costarea
from .models import Consumer,House,InvoiceCostarea
from .forms import CompanyForm,LocationForm,AreaForm,SmartmeterForm,SmartmeterPortForm,BrandandManufacturerForm
from .forms import SmartmeterLinkDeviceForm,CostareaForm,HouseForm,ConsumerForm,InvoiceForm
import random
import mysql.connector
from django.db import connection

# Create your views here.
def index(request):
    print("in index ")
    return HttpResponse('Hello, welcome to the index page.')

def create_table():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='ems_database',
                                             user='adisa',
                                             password='Adwait_14')


        my_sql_create_table_query = "CREATE TABLE Consumption15 (channel_id int(11) NOT NULL DEFAULT -1,"\
                                    "readingdate DATE NOT NULL DEFAULT 0,"\
                                    "time_0015 int(11) default 0,time_0030 int(11) default 0,time_0045 int(11) default 0,time_0100 int(11) default 0,"\
                                    "time_0115 int(11) default 0,time_0130 int(11) default 0,time_0145 int(11) default 0,time_0200 int(11) default 0,"\
                                    "time_0215 int(11) default 0,time_0230 int(11) default 0,time_0245 int(11) default 0,time_0300 int(11) default 0,"\
                                    "time_0315 int(11) default 0,time_0330 int(11) default 0,time_0345 int(11) default 0,time_0400 int(11) default 0,"\
                                    "time_0415 int(11) default 0,time_0430 int(11) default 0,time_0445 int(11) default 0,time_0500 int(11) default 0,"\
                                    "time_0515 int(11) default 0,time_0530 int(11) default 0,time_0545 int(11) default 0,time_0600 int(11) default 0,"\
                                    "time_0615 int(11) default 0,time_0630 int(11) default 0,time_0645 int(11) default 0,time_0700 int(11) default 0,"\
                                    "time_0715 int(11) default 0,time_0730 int(11) default 0,time_0745 int(11) default 0,time_0800 int(11) default 0,"\
                                    "time_0815 int(11) default 0,time_0830 int(11) default 0,time_0845 int(11) default 0,time_0900 int(11) default 0,"\
                                    "time_0915 int(11) default 0,time_0930 int(11) default 0,time_0945 int(11) default 0,time_1000 int(11) default 0,"\
                                    "time_1015 int(11) default 0,time_1030 int(11) default 0,time_1045 int(11) default 0,time_1100 int(11) default 0,"\
                                    "time_1115 int(11) default 0,time_1130 int(11) default 0,time_1145 int(11) default 0,time_1200 int(11) default 0,"\
                                    "time_1215 int(11) default 0,time_1230 int(11) default 0,time_1245 int(11) default 0,time_1300 int(11) default 0,"\
                                    "time_1315 int(11) default 0,time_1330 int(11) default 0,time_1345 int(11) default 0,time_1400 int(11) default 0,"\
                                    "time_1415 int(11) default 0,time_1430 int(11) default 0,time_1445 int(11) default 0,time_1500 int(11) default 0,"\
                                    "time_1515 int(11) default 0,time_1530 int(11) default 0,time_1545 int(11) default 0,time_1600 int(11) default 0,"\
                                    "time_1615 int(11) default 0,time_1630 int(11) default 0,time_1645 int(11) default 0,time_1700 int(11) default 0,"\
                                    "time_1715 int(11) default 0,time_1730 int(11) default 0,time_1745 int(11) default 0,time_1800 int(11) default 0,"\
                                    "time_1815 int(11) default 0,time_1830 int(11) default 0,time_1845 int(11) default 0,time_1900 int(11) default 0,"\
                                    "time_1915 int(11) default 0,time_1930 int(11) default 0,time_1945 int(11) default 0,time_2000 int(11) default 0,"\
                                    "time_2015 int(11) default 0,time_2030 int(11) default 0,time_2045 int(11) default 0,time_2100 int(11) default 0,"\
                                    "time_2115 int(11) default 0,time_2130 int(11) default 0,time_2145 int(11) default 0,time_2200 int(11) default 0,"\
                                    "time_2215 int(11) default 0,time_2230 int(11) default 0,time_2245 int(11) default 0,time_2300 int(11) default 0,"\
                                    "time_2315 int(11) default 0,time_2330 int(11) default 0,time_2345 int(11) default 0,time_0000 int(11) default 0,"\
                                    "totalday int(11) default 0,peakvalue int(11) default 0,"\
                                    "time TIME default 0 ,last_reading int(11) default 0,"\
                                    "minvalue int(11) default 0,total_reading int(11) NOT NULL default 0,"\
                                    "PRIMARY KEY  (channel_id,readingdate))"
        cursor = connection.cursor()
        #sql = "DROP TABLE IF EXISTS Consumption15"
        #cursor.execute(sql)
        cursor.execute("""SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO" """)
        result = cursor.execute(my_sql_create_table_query)
        print("Consumption15 Table created successfully ")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def insert_varibles_into_table(channel_id,readingdate,
                               tm_0015,tm_0030,tm_0045,tm_0100,tm_0115,tm_0130,tm_0145,tm_0200,tm_0215,tm_0230,tm_0245,tm_0300,
                               tm_0315,tm_0330,tm_0345,tm_0400,tm_0415,tm_0430,tm_0445,tm_0500,tm_0515,tm_0530,tm_0545,tm_0600,
                               tm_0615,tm_0630,tm_0645,tm_0700,tm_0715,tm_0730,tm_0745,tm_0800,tm_0815,tm_0830,tm_0845,tm_0900,
                               tm_0915,tm_0930,tm_0945,tm_1000,tm_1015,tm_1030,tm_1045,tm_1100,tm_1115,tm_1130,tm_1145,tm_1200,
                               tm_1215,tm_1230,tm_1245,tm_1300,tm_1315,tm_1330,tm_1345,tm_1400,tm_1415,tm_1430,tm_1445,tm_1500,
                               tm_1515,tm_1530,tm_1545,tm_1600,tm_1615,tm_1630,tm_1645,tm_1700,tm_1715,tm_1730,tm_1745,tm_1800,
                               tm_1815,tm_1830,tm_1845,tm_1900,tm_1915,tm_1930,tm_1945,tm_2000,tm_2015,tm_2030,tm_2045,tm_2100,
                               tm_2115,tm_2130,tm_2145,tm_2200,tm_2215,tm_2230,tm_2245,tm_2300,tm_2315,tm_2330,tm_2345,tm_0000,
                               totalday,peakvalue,time,last_reading,minvalue,total_reading):
   # print("hello")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='ems_database',
                                             user='adisa',
                                             password='Adwait_14')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Consumption15 (channel_id,readingdate,time_0015,time_0030,time_0045,time_0100,time_0115,time_0130,time_0145,time_0200,time_0215,time_0230,time_0245,time_0300,
        time_0315,time_0330,time_0345,time_0400,time_0415,time_0430,time_0445,time_0500,time_0515,time_0530,time_0545,time_0600,
        time_0615,time_0630,time_0645,time_0700,time_0715,time_0730,time_0745,time_0800,time_0815,time_0830,time_0845,time_0900,
        time_0915,time_0930,time_0945,time_1000,time_1015,time_1030,time_1045,time_1100,time_1115,time_1130,time_1145,time_1200,
        time_1215,time_1230,time_1245,time_1300,time_1315,time_1330,time_1345,time_1400,time_1415,time_1430,time_1445,time_1500,
        time_1515,time_1530,time_1545,time_1600,time_1615,time_1630,time_1645,time_1700,time_1715,time_1730,time_1745,time_1800,
        time_1815,time_1830,time_1845,time_1900,time_1915,time_1930,time_1945,time_2000,time_2015,time_2030,time_2045,time_2100,
        time_2115,time_2130,time_2145,time_2200,time_2215,time_2230,time_2245,time_2300,time_2315,time_2330,time_2345,time_0000,
        totalday,peakvalue,time,last_reading,minvalue,total_reading) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

        record = (channel_id,readingdate,tm_0015,tm_0030,tm_0045,tm_0100,tm_0115,tm_0130,tm_0145,tm_0200,tm_0215,tm_0230,tm_0245,tm_0300,
                               tm_0315,tm_0330,tm_0345,tm_0400,tm_0415,tm_0430,tm_0445,tm_0500,tm_0515,tm_0530,tm_0545,tm_0600,
                               tm_0615,tm_0630,tm_0645,tm_0700,tm_0715,tm_0730,tm_0745,tm_0800,tm_0815,tm_0830,tm_0845,tm_0900,
                               tm_0915,tm_0930,tm_0945,tm_1000,tm_1015,tm_1030,tm_1045,tm_1100,tm_1115,tm_1130,tm_1145,tm_1200,
                               tm_1215,tm_1230,tm_1245,tm_1300,tm_1315,tm_1330,tm_1345,tm_1400,tm_1415,tm_1430,tm_1445,tm_1500,tm_1515,tm_1530,tm_1545,tm_1600,tm_1615,tm_1630,tm_1645,tm_1700,
                               tm_1715,tm_1730,tm_1745,tm_1800,tm_1815,tm_1830,tm_1845,tm_1900,tm_1915,tm_1930,tm_1945,tm_2000,
                               tm_2015,tm_2030,tm_2045,tm_2100,tm_2115,tm_2130,tm_2145,tm_2200,tm_2215,tm_2230,tm_2245,tm_2300,
                               tm_2315,tm_2330,tm_2345,tm_0000,totalday,peakvalue,time,last_reading,minvalue,total_reading)

        cursor.execute(mySql_insert_query, record)
        connection.commit()

    except mysql.connector.Error as error:
        print("record failed:",record)
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        #    print("MySQL connection is closed")

def select_query():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='ems_database',
                                             user='adisa',
                                             password='Adwait_14')

        sql_select_Query = "select * from Consumption15"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        #print("\nPrinting each row")
        #for row in records:
        #    print("channel_Id = ", row[0], )
        #    print("readingdate = ", row[1])
        #    print("time_0015 = ", row[2])
        #    print("time_0030  = ", row[3], "\n")

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def txt_to_list(filename):
    a_file = open(filename, "r")
    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)

    a_file.close()
    #print(list_of_lists)
    return list_of_lists

def remove_brackets(record):
    #print("record:",record)
    #temp_str = str(record)[1:-1]       # get list with square brackets
    #temp_str2 = str(temp_str).rstrip(',')     # remove end comma
    #print("temp_str:",temp_str2)
    for i in record:
        t1 = str(i).strip()
        t1_list = t1.split(",")
        data_array = []
        opening_bracket = '["'
        closing_bracket = '"]'
        for j in t1_list:
            if opening_bracket in j:
                j = j.replace('["',"")
                j = j.replace('(', "")
            elif closing_bracket in j:
                j = j.replace('"]',"")
               # j = j.replace(')', "")
            elif "(" in j:
                j = j.replace("(","")
            elif ")" in j:
                #print("j:",j)
                j = j.replace(")","")
            data_array.append(j)
            #print(data_array)

    return data_array

def showconsumption(request):
    create_table()
    #records_to_insert = txt_to_list('/home/adisa/projects/ems/site_ems/consumption15_2.txt')
    records_to_insert = txt_to_list('/home/adisa/projects/ems/site_ems/consumption15.txt')
    print("length of list:", len(records_to_insert))
    for record in records_to_insert:
        data_array = remove_brackets(record)
        # print(data_array)
        for i in range(0, len(data_array) - 1):
            quotes = "'"
            # print("data_array[i]:",data_array[i])
            if quotes in data_array[i]:
                data_array[i] = data_array[i].replace("'", "")
                data_array[i] = data_array[i]
            else:
                data_array[i] = int(data_array[i])

        #  print("data array:",data_array,type(data_array))
        consumption_arr = []
        consumption_arr = data_array[2:98]
        peakvalue = max(consumption_arr)
        minvalue = min(consumption_arr)
        last_reading = consumption_arr[95]
        # print("length of consumption arr:",len(consumption_arr))
        # print("consumption array:",consumption_arr)
        # print("max:",max(consumption_arr))
        # print("min:",min(consumption_arr))
        # print("last reading:",consumption_arr[95])
        totalday = 0
        for ele in range(0, len(consumption_arr)):
            totalday = totalday + consumption_arr[ele]
        # print("Total of the day:",total)
        insert_varibles_into_table(data_array[0], data_array[1], data_array[2], data_array[3], data_array[4],
                                   data_array[5], data_array[6], data_array[7], data_array[8], data_array[9],
                                   data_array[10], data_array[11], data_array[12], data_array[13], data_array[14],
                                   data_array[15], data_array[16], data_array[17], data_array[18],
                                   data_array[19], data_array[20], data_array[21], data_array[22], data_array[23],
                                   data_array[24], data_array[25], data_array[26], data_array[27],
                                   data_array[28], data_array[29], data_array[30], data_array[31], data_array[32],
                                   data_array[33], data_array[34], data_array[35], data_array[36],
                                   data_array[37], data_array[38], data_array[39], data_array[40], data_array[41],
                                   data_array[42], data_array[43], data_array[44], data_array[45],
                                   data_array[46], data_array[47], data_array[48], data_array[49], data_array[50],
                                   data_array[51], data_array[52], data_array[53], data_array[54],
                                   data_array[55], data_array[56], data_array[57], data_array[58], data_array[59],
                                   data_array[60], data_array[61], data_array[62], data_array[63],
                                   data_array[64], data_array[65], data_array[66], data_array[67], data_array[68],
                                   data_array[69], data_array[70], data_array[71], data_array[72],
                                   data_array[73], data_array[74], data_array[75], data_array[76], data_array[77],
                                   data_array[78], data_array[79], data_array[80], data_array[81],
                                   data_array[82], data_array[83], data_array[84], data_array[85], data_array[86],
                                   data_array[87], data_array[88], data_array[89], data_array[90],
                                   data_array[91], data_array[92], data_array[93], data_array[94], data_array[95],
                                   data_array[96], data_array[97], totalday, peakvalue,
                                   data_array[100], last_reading, minvalue, data_array[103])
    select_query()

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Consumption15")
        row = cursor.fetchall()
    #print("row:",row)
    return render(request,'showconsumption.html',{'data':row})

def consumption_graph(request):
    randomlist = []
    for i in range(0, 50):
        n = random.randint(1000, 9999)
        randomlist.append(n)
    print(randomlist)
    return render(request,'consumption_graph.html',{'data_set':randomlist})

def addcostarea(request):
    if request.method == "POST":
        form = CostareaForm(request.POST)
        if form.is_valid():
                Costarea = form.save(commit=False)
                Costarea.createdby = request.user
                Costarea.modifiedby = request.user
                Costarea = Costarea.save()
                print(" form is valid and in try block")
                return redirect('Cost_center/showcostarea')
    else:
        print("in else part")
        form = CostareaForm()
    return render(request,'Cost_center/costarea.html',{'form':form})

def showcostarea(request):
    obj = Costarea.objects.all()
    cnm_list = Company.objects.all()
    lnm_list = Location.objects.all()
    return render(request,'Cost_center/showcostarea.html',{'data':obj,'cnm_list':cnm_list,'lnm_list':lnm_list})

def addhouse(request):
    if request.method == "POST":
        form = HouseForm(request.POST)
        if form.is_valid():
                House = form.save(commit=False)
                House.createdby = request.user
                House.modifiedby = request.user
                House = House.save()
                print(" form is valid and in try block")
                return redirect('Cost_center/showhouse')
    else:
        print("in else part")
        form = HouseForm()
    return render(request,'Cost_center/house.html',{'form':form})

def showhouse(request):
    obj = House.objects.all()
    cnm_list = Company.objects.all()
    lnm_list = Location.objects.all()
    return render(request,'Cost_center/showhouse.html',{'data':obj,'cnm_list':cnm_list,'lnm_list':lnm_list})

def addconsumerobj(request):
    if request.method == "POST":
        form = ConsumerForm(request.POST)
        if form.is_valid():
                Consumer = form.save(commit=False)
                Consumer.createdby = request.user
                Consumer.modifiedby = request.user
                Consumer = Consumer.save()
                print(" form is valid and in try block")
                return redirect('Cost_center/showconsumerobj')
    else:
        print("in else part")
        form = ConsumerForm()
    return render(request,'Cost_center/consumerobject.html',{'form':form})

def showconsumerobj(request):
    obj = Consumer.objects.all()
    cnm_list = Company.objects.all()
    lnm_list = Location.objects.all()
    ca_list = Costarea.objects.all()
    house_list = House.objects.all()
    return render(request,'Cost_center/showconsumerobj.html',{'data':obj,'cnm_list':cnm_list,
                           'lnm_list':lnm_list,'ca_list':ca_list,'house_list':house_list})

def invoice(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
                InvoiceCostarea = form.save(commit=False)
                InvoiceCostarea.createdby = request.user
                InvoiceCostarea.modifiedby = request.user
                InvoiceCostarea = InvoiceCostarea.save()
                print(" form is valid and in try block")
                return redirect('Cost_center/showinvoice')
    else:
        print("in else part")
        form = InvoiceForm()
    return render(request,'Cost_center/invoice.html',{'form':form})

def showinvoice(request):
    #consumer_nm = InvoiceCostarea.objects.filter()
    return render(request,'Cost_center/showinvoice.html')


def addsmscreen(request):
    if request.method == "POST":
        form = SmartmeterForm(request.POST)
        if form.is_valid():
                Smartmeter = form.save(commit=False)
                Smartmeter.createdby = request.user
                Smartmeter.modifiedby = request.user
                Smartmeter = Smartmeter.save()
                print(" form is valid and in try block")
                return redirect('Smart_meter/showsmscreen')
    else:
        print("in else part")
        form = SmartmeterForm()
    return render(request,'Smart_meter/addsmscreen.html',{'form':form})

def showsmscreen(request):
    result = Smartmeter.objects.all()
    return render(request, 'Smart_meter/showsmscreen.html', {'result': result})

def addsmport(request):
    form = SmartmeterPortForm()
    if request.method == "POST":
        form = SmartmeterPortForm(request.POST)
        if form.is_valid():
                SmartmeterPort = form.save(commit=False)
                SmartmeterPort.createdby = request.user
                SmartmeterPort.modifiedby = request.user
                SmartmeterPort = SmartmeterPort.save()
                print(" form is valid and in try block")
                return redirect('Smart_meter/showsmport')
    else:
        print("in else part")
        form = SmartmeterPortForm()
    return render(request,"Smart_meter/addsmport.html",{'form':form})

def showsmport(request):
    obj = SmartmeterPort.objects.all()
    return render(request,'Smart_meter/showsmport.html',{'result':obj})

def editsmartmeter(request, id):
    obj = Location.objects.get(location_id=id)
    updated_on = obj.modifieddate
    return render(request, 'editlocation.html', {'employee': obj, 'updated_on': updated_on})

def addsmlink(request):
    form = SmartmeterLinkDeviceForm()
    if request.method == "POST":
                # = form.save(commit=False)
                #SmartmeterPort.createdby = request.user
                #SmartmeterPort.modifiedby = request.user
                #SmartmeterPort = SmartmeterPort.save()
                print(" form is valid and in try block")
                return redirect('Smart_meter/showsmlink')
    else:
        print("in else part")
        form = SmartmeterLinkDeviceForm()
    return render(request,"Smart_meter/addsmlink.html",{'form':form})

def showsmlink(request):
    obj = Smartmeter.objects.all()
    return render(request,"Smart_meter/showsmlink.html",{'result':obj})

def sm_brand_n_manf(request):
    return render(request,'Smart_meter/sm_brand_n_manf.html')

def addsmoverview(request):
    if request.method == "POST":
        form = SmartmeterForm(request.POST)
        if form.is_valid():
                Smartmeter = form.save(commit=False)
                Smartmeter.createdby = request.user
                Smartmeter.modifiedby = request.user
                Smartmeter = Smartmeter.save()
                print(" form is valid and in try block")
                return redirect('Smart_meter/showsmoverview')
    else:
        print("in else part")
        form = SmartmeterForm()
    return render(request,'Smart_meter/addsmoverview.html',{'form':form})

def showsmoverview(request):
    return render(request,'Smart_meter/showsmoverview.html')

def sm_device_address(request):
    return render(request,'Smart_meter/sm_device_address.html')

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
    return render(request,'editlocation.html', {
        'cnm_list':cnm_list,
        'employee':obj,
        'updated_on':updated_on
    })

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
    lnm_list = Location.objects.all()
    return render(request, 'showarea.html',{'result':result, 'lnm_list': lnm_list})

def load_location(request):
    company_id = request.GET.get('company_id')
    locations = Company.objects.filter(company_id=company_id).all()
    return render(request, 'location_dropdown.html', {'locations': locations})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def editarea(request, id):
    obj = Area.objects.get(area_id=id)
    print("obj:", obj)
    #cnm_list = get_company_list()
    cnm_list = Company.objects.all()
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
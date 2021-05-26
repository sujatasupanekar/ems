from django.db import models

# Create your models here.

class Brand_and_Manufacturer(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=30)
    brand_model = models.CharField(max_length=50)
    brand_type = models.PositiveSmallIntegerField()
    manufacturer = models.CharField(max_length=50)
    description = models.TextField()
    max_no_of_channels = models.IntegerField()
    createdby = models.CharField(max_length=50, default=None)
    createddate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modifiedby = models.CharField(max_length=50, default=None)
    modifieddate = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return (self.brand_name + self.manufacturer)

class Company(models.Model):
    #consortium = models.CharField(max_length=10)
    company_id = models.AutoField(primary_key=True)
    short_name = models.CharField(max_length=15)
    company_name1 = models.CharField(max_length=30)
    company_name2 = models.CharField(max_length=30, blank=True, null=True)
    street = models.TextField()
    country_code = models.CharField(max_length=3)
    zip_code = models.CharField(max_length=6, blank=True, null=True)
    town = models.CharField(max_length=20)
    country = models.CharField(max_length=30, blank=True, null=True)
    contact_person = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    tel_no = models.CharField(max_length=15)
    fax_no = models.CharField(max_length=15)
    company_logo = models.IntegerField()
    company_url = models.CharField(max_length=40, blank=True, null=True)
    createdby = models.CharField(max_length=50,default=None)
    createddate = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modifiedby = models.CharField(max_length=50,default=None)
    modifieddate = models.DateTimeField(auto_now=True,null=True,blank=True)
    tax_no1 = models.CharField(max_length=40)
    tax_no2 = models.CharField(max_length=40)

    def __str__(self):
        return self.company_name1

class Consortium(models.Model):
    consortium_id = models.AutoField(primary_key=True)
    short_name = models.CharField(unique=True, max_length=15)
    consortium_name1 = models.CharField(max_length=30, blank=True, null=True)
    consortium_name2 = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    town = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    contact_person = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    tel_no = models.CharField(max_length=15, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    energy_type = models.SmallIntegerField(blank=True, null=True)
    usable = models.CharField(max_length=1, blank=True, null=True)
    createdby = models.CharField(max_length=50, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50, blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    consortium_logo = models.IntegerField(blank=True, null=True)
    tax_no1 = models.CharField(max_length=40)
    tax_no2 = models.CharField(max_length=40)

class Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    location_id = models.AutoField(primary_key=True)
    short_name = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    zip_code = models.CharField(max_length=6, blank=True, null=True)
    town = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    contact_person = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    tel_no = models.CharField(max_length=15, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    #penalty_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    #penalty_limit = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    #provider_id = models.IntegerField(blank=True, null=True)
    #energy_id = models.IntegerField(blank=True, null=True)
    #free_client = models.CharField(max_length=1, blank=True, null=True)
    #billing_id = models.PositiveIntegerField(blank=True, null=True)
    #contact_id = models.IntegerField(blank=True, null=True)
    #remarks = models.CharField(max_length=120, blank=True, null=True)
    #invoice_marker = models.CharField(max_length=10, blank=True, null=True)
    #residential_provider_id = models.IntegerField(blank=True, null=True)
    #residential_billing_id = models.IntegerField(blank=True, null=True)
    #location_type = models.CharField(max_length=25, blank=True, null=True)
    #state = models.CharField(max_length=1, blank=True, null=True)
    #usable = models.CharField(max_length=1)
    createdby = models.CharField(max_length=50, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    modifiedby = models.CharField(max_length=50, blank=True, null=True)
    modifieddate = models.DateTimeField(blank=True, null=True)
    location_logo = models.IntegerField(blank=True, null=True)
    #contentright = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.short_name

class Area(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL ,null=True)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL,null= True)
    area_id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=50)
    area_logo = models.CharField(max_length=100)
    createdby = models.CharField(max_length=50, default=None)
    createddate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modifiedby = models.CharField(max_length=50, default=None)
    modifieddate = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return (self.company + self.location + self.area)

class Smartmeter(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    smartmeter_id = models.AutoField(primary_key=True)
    short_name = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    brand_id = models.PositiveSmallIntegerField()
    parent_smartmeter_id = models.PositiveSmallIntegerField(blank=True,null=True)
    max_no_of_channels = models.IntegerField(blank=True,null=True)
    createdby = models.CharField(max_length=50, default=None)
    createddate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modifiedby = models.CharField(max_length=50, default=None)
    modifieddate = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return (self.smartmeter_id + self.parent_smartmeter_id)

class SmartmeterPort(models.Model):
    port_type_choices = [('RS232', 'RS232'), ('RS485', 'RS485'), ('Network', 'Network')]
    communication_type_choices = [('serial', 'Serial'), ('tcp/ip', 'TCP/IP')]
    parity_choices = [('even', "Even"), ('odd', 'Odd')]
    flow_control_choices = [('xon', 'X on'), ('X off', 'X off')]
    data_bit_choices = [tuple([x, x]) for x in range(1, 32)]
    baud_rate_choices = [tuple([x, x]) for x in range(1, 32)]
    stop_bit_choices = [tuple([x, x]) for x in range(1, 5)]
    reading_type_choices = [('Local server', 'Direct'), ('remote server', 'PC')]

    port_type = models.CharField(max_length=10,choices=port_type_choices,default=None)
    communication_type = models.CharField(max_length=10,choices=communication_type_choices,default=None)
    device_id = models.CharField(max_length=20)
    device_password = models.CharField(max_length=15, blank=True, null=True)
    device_address = models.CharField(max_length=30)
    device_type = models.IntegerField()
    reading_type = models.CharField(max_length=20,choices=reading_type_choices)
    communication_id = models.PositiveIntegerField()
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    lan_port = models.IntegerField(blank=True, null=True)
    baud_rate = models.BooleanField(max_length=10, choices=baud_rate_choices ,blank=True, null=True)
    data_bits = models.BooleanField(max_length=2, choices=data_bit_choices, blank=True, null=True)
    parity = models.BooleanField(max_length=10, choices=parity_choices,blank=True, null=True)
    stop_bits = models.BooleanField(max_length=4, choices=stop_bit_choices, blank=True, null=True)
    flow_control = models.BooleanField(max_length=5,choices=flow_control_choices, blank=True, null=True)
    modem_port = models.CharField(max_length=10, blank=True, null=True)
    createdby = models.CharField(max_length=50, default=None)
    createddate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modifiedby = models.CharField(max_length=50, default=None)
    modifieddate = models.DateTimeField(auto_now=True, null=True, blank=True)
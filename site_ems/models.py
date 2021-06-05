from django.db import models

# Create your models here.

class Brand_and_Manufacturer(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=30)
    brand_model = models.CharField(max_length=50)
    brand_type = models.PositiveSmallIntegerField()
    manufacturer = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
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
    short_name = models.CharField(max_length=15, default="company short")
    company_name1 = models.CharField(max_length=30, default="company_name1")
    company_name2 = models.CharField(max_length=30, blank=True, null=True, default="company name 2")
    street = models.CharField(max_length=50, default="company steet name")
    country_code = models.CharField(max_length=3, default="91")
    zip_code = models.CharField(max_length=6, blank=True, null=True, default="416416")
    town = models.CharField(max_length=20, default="sangli")
    country = models.CharField(max_length=30, blank=True, null=True, default="India")
    contact_person = models.CharField(max_length=30, default="SalesPersonName")
    email = models.CharField(max_length=40, default="info@ems.com")
    tel_no = models.CharField(max_length=15, default="+91987654321")
    fax_no = models.CharField(max_length=15, default="+918888888888")
    company_logo = models.IntegerField(default=5)
    company_url = models.CharField(max_length=40, blank=True, null=True, default="https://www.ems.com")
    createdby = models.CharField(max_length=50,default="person1")
    createddate = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modifiedby = models.CharField(max_length=50,default="person2")
    modifieddate = models.DateTimeField(auto_now=True,null=True,blank=True)
    tax_no1 = models.CharField(max_length=40, default="10")
    tax_no2 = models.CharField(max_length=40, default="50")

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
    short_name = models.CharField(max_length=15, blank=True, null=True, default="ShortLocNm")
    description = models.CharField(max_length=30, blank=True, null=True, default="location description")
    street = models.CharField(max_length=30, blank=True, null=True, default="company street name")
    country_code = models.CharField(max_length=3, blank=True, null=True, default="91")
    zip_code = models.CharField(max_length=6, blank=True, null=True, default="416146")
    town = models.CharField(max_length=20, blank=True, null=True, default="vishrambag")
    country = models.CharField(max_length=30, blank=True, null=True, default="India")
    contact_person = models.CharField(max_length=30, blank=True, null=True, default="SalesRepName")
    email = models.CharField(max_length=40, blank=True, null=True, default="location_contact@ems.com")
    tel_no = models.CharField(max_length=15, blank=True, null=True, default="+919999999999")
    fax_no = models.CharField(max_length=15, blank=True, null=True, default="+91888888888")
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
    createdby = models.CharField(max_length=50,default="person1")
    createddate = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modifiedby = models.CharField(max_length=50,default="person2")
    modifieddate = models.DateTimeField(auto_now=True,null=True,blank=True)
    location_logo = models.IntegerField(blank=True, null=True, default=10)
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

    #def __str__(self):
    #    return (self.company + self.location + self.area)

class Consumption05(models.Model):
    channel_id = models.IntegerField(primary_key=True)
    readingdate = models.DateField()
    field_0005 = models.BigIntegerField(db_column='_0005', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0010 = models.BigIntegerField(db_column='_0010', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0015 = models.BigIntegerField(db_column='_0015', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0020 = models.BigIntegerField(db_column='_0020', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0025 = models.BigIntegerField(db_column='_0025', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0030 = models.BigIntegerField(db_column='_0030', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0035 = models.BigIntegerField(db_column='_0035', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0040 = models.BigIntegerField(db_column='_0040', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0045 = models.BigIntegerField(db_column='_0045', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0050 = models.BigIntegerField(db_column='_0050', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0055 = models.BigIntegerField(db_column='_0055', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0100 = models.BigIntegerField(db_column='_0100', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0105 = models.BigIntegerField(db_column='_0105', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0110 = models.BigIntegerField(db_column='_0110', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0115 = models.BigIntegerField(db_column='_0115', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0120 = models.BigIntegerField(db_column='_0120', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0125 = models.BigIntegerField(db_column='_0125', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0130 = models.BigIntegerField(db_column='_0130', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0135 = models.BigIntegerField(db_column='_0135', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0140 = models.BigIntegerField(db_column='_0140', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0145 = models.BigIntegerField(db_column='_0145', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0150 = models.BigIntegerField(db_column='_0150', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0155 = models.BigIntegerField(db_column='_0155', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0200 = models.BigIntegerField(db_column='_0200', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0205 = models.BigIntegerField(db_column='_0205', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0210 = models.BigIntegerField(db_column='_0210', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0215 = models.BigIntegerField(db_column='_0215', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0220 = models.BigIntegerField(db_column='_0220', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0225 = models.BigIntegerField(db_column='_0225', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0230 = models.BigIntegerField(db_column='_0230', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0235 = models.BigIntegerField(db_column='_0235', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0240 = models.BigIntegerField(db_column='_0240', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0245 = models.BigIntegerField(db_column='_0245', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0250 = models.BigIntegerField(db_column='_0250', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0255 = models.BigIntegerField(db_column='_0255', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0300 = models.BigIntegerField(db_column='_0300', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0305 = models.BigIntegerField(db_column='_0305', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0310 = models.BigIntegerField(db_column='_0310', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0315 = models.BigIntegerField(db_column='_0315', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0320 = models.BigIntegerField(db_column='_0320', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0325 = models.BigIntegerField(db_column='_0325', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0330 = models.BigIntegerField(db_column='_0330', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0335 = models.BigIntegerField(db_column='_0335', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0340 = models.BigIntegerField(db_column='_0340', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0345 = models.BigIntegerField(db_column='_0345', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0350 = models.BigIntegerField(db_column='_0350', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0355 = models.BigIntegerField(db_column='_0355', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0400 = models.BigIntegerField(db_column='_0400', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0405 = models.BigIntegerField(db_column='_0405', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0410 = models.BigIntegerField(db_column='_0410', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0415 = models.BigIntegerField(db_column='_0415', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0420 = models.BigIntegerField(db_column='_0420', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0425 = models.BigIntegerField(db_column='_0425', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0430 = models.BigIntegerField(db_column='_0430', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0435 = models.BigIntegerField(db_column='_0435', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0440 = models.BigIntegerField(db_column='_0440', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0445 = models.BigIntegerField(db_column='_0445', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0450 = models.BigIntegerField(db_column='_0450', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0455 = models.BigIntegerField(db_column='_0455', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0500 = models.BigIntegerField(db_column='_0500', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0505 = models.BigIntegerField(db_column='_0505', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0510 = models.BigIntegerField(db_column='_0510', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0515 = models.BigIntegerField(db_column='_0515', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0520 = models.BigIntegerField(db_column='_0520', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0525 = models.BigIntegerField(db_column='_0525', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0530 = models.BigIntegerField(db_column='_0530', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0535 = models.BigIntegerField(db_column='_0535', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0540 = models.BigIntegerField(db_column='_0540', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0545 = models.BigIntegerField(db_column='_0545', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0550 = models.BigIntegerField(db_column='_0550', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0555 = models.BigIntegerField(db_column='_0555', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0600 = models.BigIntegerField(db_column='_0600', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0605 = models.BigIntegerField(db_column='_0605', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0610 = models.BigIntegerField(db_column='_0610', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0615 = models.BigIntegerField(db_column='_0615', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0620 = models.BigIntegerField(db_column='_0620', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0625 = models.BigIntegerField(db_column='_0625', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0630 = models.BigIntegerField(db_column='_0630', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0635 = models.BigIntegerField(db_column='_0635', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0640 = models.BigIntegerField(db_column='_0640', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0645 = models.BigIntegerField(db_column='_0645', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0650 = models.BigIntegerField(db_column='_0650', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0655 = models.BigIntegerField(db_column='_0655', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0700 = models.BigIntegerField(db_column='_0700', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0705 = models.BigIntegerField(db_column='_0705', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0710 = models.BigIntegerField(db_column='_0710', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0715 = models.BigIntegerField(db_column='_0715', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0720 = models.BigIntegerField(db_column='_0720', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0725 = models.BigIntegerField(db_column='_0725', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0730 = models.BigIntegerField(db_column='_0730', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0735 = models.BigIntegerField(db_column='_0735', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0740 = models.BigIntegerField(db_column='_0740', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0745 = models.BigIntegerField(db_column='_0745', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0750 = models.BigIntegerField(db_column='_0750', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0755 = models.BigIntegerField(db_column='_0755', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0800 = models.BigIntegerField(db_column='_0800', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0805 = models.BigIntegerField(db_column='_0805', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0810 = models.BigIntegerField(db_column='_0810', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0815 = models.BigIntegerField(db_column='_0815', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0820 = models.BigIntegerField(db_column='_0820', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0825 = models.BigIntegerField(db_column='_0825', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0830 = models.BigIntegerField(db_column='_0830', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0835 = models.BigIntegerField(db_column='_0835', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0840 = models.BigIntegerField(db_column='_0840', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0845 = models.BigIntegerField(db_column='_0845', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0850 = models.BigIntegerField(db_column='_0850', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0855 = models.BigIntegerField(db_column='_0855', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0900 = models.BigIntegerField(db_column='_0900', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0905 = models.BigIntegerField(db_column='_0905', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0910 = models.BigIntegerField(db_column='_0910', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0915 = models.BigIntegerField(db_column='_0915', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0920 = models.BigIntegerField(db_column='_0920', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0925 = models.BigIntegerField(db_column='_0925', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0930 = models.BigIntegerField(db_column='_0930', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0935 = models.BigIntegerField(db_column='_0935', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0940 = models.BigIntegerField(db_column='_0940', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0945 = models.BigIntegerField(db_column='_0945', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0950 = models.BigIntegerField(db_column='_0950', blank=True, null=True)  # Field renamed because it started with '_'.
    field_0955 = models.BigIntegerField(db_column='_0955', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1000 = models.BigIntegerField(db_column='_1000', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1005 = models.BigIntegerField(db_column='_1005', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1010 = models.BigIntegerField(db_column='_1010', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1015 = models.BigIntegerField(db_column='_1015', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1020 = models.BigIntegerField(db_column='_1020', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1025 = models.BigIntegerField(db_column='_1025', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1030 = models.BigIntegerField(db_column='_1030', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1035 = models.BigIntegerField(db_column='_1035', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1040 = models.BigIntegerField(db_column='_1040', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1045 = models.BigIntegerField(db_column='_1045', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1050 = models.BigIntegerField(db_column='_1050', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1055 = models.BigIntegerField(db_column='_1055', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1100 = models.BigIntegerField(db_column='_1100', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1105 = models.BigIntegerField(db_column='_1105', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1110 = models.BigIntegerField(db_column='_1110', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1115 = models.BigIntegerField(db_column='_1115', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1120 = models.BigIntegerField(db_column='_1120', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1125 = models.BigIntegerField(db_column='_1125', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1130 = models.BigIntegerField(db_column='_1130', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1135 = models.BigIntegerField(db_column='_1135', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1140 = models.BigIntegerField(db_column='_1140', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1145 = models.BigIntegerField(db_column='_1145', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1150 = models.BigIntegerField(db_column='_1150', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1155 = models.BigIntegerField(db_column='_1155', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1200 = models.BigIntegerField(db_column='_1200', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1205 = models.BigIntegerField(db_column='_1205', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1210 = models.BigIntegerField(db_column='_1210', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1215 = models.BigIntegerField(db_column='_1215', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1220 = models.BigIntegerField(db_column='_1220', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1225 = models.BigIntegerField(db_column='_1225', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1230 = models.BigIntegerField(db_column='_1230', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1235 = models.BigIntegerField(db_column='_1235', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1240 = models.BigIntegerField(db_column='_1240', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1245 = models.BigIntegerField(db_column='_1245', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1250 = models.BigIntegerField(db_column='_1250', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1255 = models.BigIntegerField(db_column='_1255', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1300 = models.BigIntegerField(db_column='_1300', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1305 = models.BigIntegerField(db_column='_1305', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1310 = models.BigIntegerField(db_column='_1310', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1315 = models.BigIntegerField(db_column='_1315', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1320 = models.BigIntegerField(db_column='_1320', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1325 = models.BigIntegerField(db_column='_1325', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1330 = models.BigIntegerField(db_column='_1330', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1335 = models.BigIntegerField(db_column='_1335', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1340 = models.BigIntegerField(db_column='_1340', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1345 = models.BigIntegerField(db_column='_1345', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1350 = models.BigIntegerField(db_column='_1350', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1355 = models.BigIntegerField(db_column='_1355', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1400 = models.BigIntegerField(db_column='_1400', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1405 = models.BigIntegerField(db_column='_1405', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1410 = models.BigIntegerField(db_column='_1410', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1415 = models.BigIntegerField(db_column='_1415', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1420 = models.BigIntegerField(db_column='_1420', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1425 = models.BigIntegerField(db_column='_1425', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1430 = models.BigIntegerField(db_column='_1430', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1435 = models.BigIntegerField(db_column='_1435', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1440 = models.BigIntegerField(db_column='_1440', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1445 = models.BigIntegerField(db_column='_1445', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1450 = models.BigIntegerField(db_column='_1450', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1455 = models.BigIntegerField(db_column='_1455', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1500 = models.BigIntegerField(db_column='_1500', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1505 = models.BigIntegerField(db_column='_1505', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1510 = models.BigIntegerField(db_column='_1510', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1515 = models.BigIntegerField(db_column='_1515', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1520 = models.BigIntegerField(db_column='_1520', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1525 = models.BigIntegerField(db_column='_1525', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1530 = models.BigIntegerField(db_column='_1530', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1535 = models.BigIntegerField(db_column='_1535', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1540 = models.BigIntegerField(db_column='_1540', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1545 = models.BigIntegerField(db_column='_1545', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1550 = models.BigIntegerField(db_column='_1550', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1555 = models.BigIntegerField(db_column='_1555', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1600 = models.BigIntegerField(db_column='_1600', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1605 = models.BigIntegerField(db_column='_1605', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1610 = models.BigIntegerField(db_column='_1610', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1615 = models.BigIntegerField(db_column='_1615', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1620 = models.BigIntegerField(db_column='_1620', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1625 = models.BigIntegerField(db_column='_1625', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1630 = models.BigIntegerField(db_column='_1630', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1635 = models.BigIntegerField(db_column='_1635', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1640 = models.BigIntegerField(db_column='_1640', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1645 = models.BigIntegerField(db_column='_1645', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1650 = models.BigIntegerField(db_column='_1650', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1655 = models.BigIntegerField(db_column='_1655', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1700 = models.BigIntegerField(db_column='_1700', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1705 = models.BigIntegerField(db_column='_1705', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1710 = models.BigIntegerField(db_column='_1710', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1715 = models.BigIntegerField(db_column='_1715', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1720 = models.BigIntegerField(db_column='_1720', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1725 = models.BigIntegerField(db_column='_1725', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1730 = models.BigIntegerField(db_column='_1730', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1735 = models.BigIntegerField(db_column='_1735', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1740 = models.BigIntegerField(db_column='_1740', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1745 = models.BigIntegerField(db_column='_1745', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1750 = models.BigIntegerField(db_column='_1750', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1755 = models.BigIntegerField(db_column='_1755', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1800 = models.BigIntegerField(db_column='_1800', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1805 = models.BigIntegerField(db_column='_1805', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1810 = models.BigIntegerField(db_column='_1810', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1815 = models.BigIntegerField(db_column='_1815', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1820 = models.BigIntegerField(db_column='_1820', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1825 = models.BigIntegerField(db_column='_1825', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1830 = models.BigIntegerField(db_column='_1830', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1835 = models.BigIntegerField(db_column='_1835', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1840 = models.BigIntegerField(db_column='_1840', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1845 = models.BigIntegerField(db_column='_1845', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1850 = models.BigIntegerField(db_column='_1850', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1855 = models.BigIntegerField(db_column='_1855', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1900 = models.BigIntegerField(db_column='_1900', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1905 = models.BigIntegerField(db_column='_1905', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1910 = models.BigIntegerField(db_column='_1910', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1915 = models.BigIntegerField(db_column='_1915', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1920 = models.BigIntegerField(db_column='_1920', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1925 = models.BigIntegerField(db_column='_1925', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1930 = models.BigIntegerField(db_column='_1930', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1935 = models.BigIntegerField(db_column='_1935', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1940 = models.BigIntegerField(db_column='_1940', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1945 = models.BigIntegerField(db_column='_1945', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1950 = models.BigIntegerField(db_column='_1950', blank=True, null=True)  # Field renamed because it started with '_'.
    field_1955 = models.BigIntegerField(db_column='_1955', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2000 = models.BigIntegerField(db_column='_2000', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2005 = models.BigIntegerField(db_column='_2005', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2010 = models.BigIntegerField(db_column='_2010', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2015 = models.BigIntegerField(db_column='_2015', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2020 = models.BigIntegerField(db_column='_2020', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2025 = models.BigIntegerField(db_column='_2025', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2030 = models.BigIntegerField(db_column='_2030', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2035 = models.BigIntegerField(db_column='_2035', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2040 = models.BigIntegerField(db_column='_2040', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2045 = models.BigIntegerField(db_column='_2045', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2050 = models.BigIntegerField(db_column='_2050', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2055 = models.BigIntegerField(db_column='_2055', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2100 = models.BigIntegerField(db_column='_2100', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2105 = models.BigIntegerField(db_column='_2105', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2110 = models.BigIntegerField(db_column='_2110', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2115 = models.BigIntegerField(db_column='_2115', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2120 = models.BigIntegerField(db_column='_2120', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2125 = models.BigIntegerField(db_column='_2125', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2130 = models.BigIntegerField(db_column='_2130', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2135 = models.BigIntegerField(db_column='_2135', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2140 = models.BigIntegerField(db_column='_2140', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2145 = models.BigIntegerField(db_column='_2145', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2150 = models.BigIntegerField(db_column='_2150', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2155 = models.BigIntegerField(db_column='_2155', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2200 = models.BigIntegerField(db_column='_2200', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2205 = models.BigIntegerField(db_column='_2205', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2210 = models.BigIntegerField(db_column='_2210', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2215 = models.BigIntegerField(db_column='_2215', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2220 = models.BigIntegerField(db_column='_2220', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2225 = models.BigIntegerField(db_column='_2225', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2230 = models.BigIntegerField(db_column='_2230', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2235 = models.BigIntegerField(db_column='_2235', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2240 = models.BigIntegerField(db_column='_2240', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2245 = models.BigIntegerField(db_column='_2245', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2250 = models.BigIntegerField(db_column='_2250', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2255 = models.BigIntegerField(db_column='_2255', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2300 = models.BigIntegerField(db_column='_2300', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2305 = models.BigIntegerField(db_column='_2305', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2310 = models.BigIntegerField(db_column='_2310', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2315 = models.BigIntegerField(db_column='_2315', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2320 = models.BigIntegerField(db_column='_2320', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2325 = models.BigIntegerField(db_column='_2325', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2330 = models.BigIntegerField(db_column='_2330', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2335 = models.BigIntegerField(db_column='_2335', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2340 = models.BigIntegerField(db_column='_2340', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2345 = models.BigIntegerField(db_column='_2345', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2350 = models.BigIntegerField(db_column='_2350', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2355 = models.BigIntegerField(db_column='_2355', blank=True, null=True)  # Field renamed because it started with '_'.
    field_2400 = models.BigIntegerField(db_column='_2400', blank=True, null=True)  # Field renamed because it started with '_'.
    totalday = models.BigIntegerField(blank=True, null=True)
    peakvalue = models.BigIntegerField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    last_reading = models.BigIntegerField(blank=True, null=True)
    minvalue = models.BigIntegerField(blank=True, null=True)
    total_reading = models.BigIntegerField()

    class Meta:
        unique_together = (('channel_id', 'readingdate'),)

class Costarea(models.Model):
    costarea_id = models.AutoField(primary_key=True)
    company_id = models.IntegerField()
    location_id = models.IntegerField()
    cost_area = models.CharField(max_length=50)
    usable = models.CharField(max_length=1)
    image_id = models.IntegerField(blank=True, null=True)
    createdby = models.CharField(max_length=50, default=None)
    createddate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modifiedby = models.CharField(max_length=50, default=None)
    modifieddate = models.DateTimeField(auto_now=True, null=True, blank=True)

class Smartmeter(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    area_id = models.ForeignKey(Area,on_delete=models.CASCADE, blank=True, null=True)
    smartmeter_id = models.AutoField(primary_key=True)
    short_name = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    brand_id = models.PositiveSmallIntegerField()
    brand_type = models.PositiveIntegerField(blank=True,null=True)
    parent_smartmeter_id = models.PositiveSmallIntegerField(blank=True,null=True)
    max_no_of_channels = models.IntegerField(blank=True,null=True)
    device_id = models.CharField(max_length=20,default="00000")
    device_password = models.CharField(max_length=15, blank=True, null=True)
    device_address = models.CharField(max_length=30,blank=True,null=True)
    communication_id = models.PositiveIntegerField(blank=True,null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    lan_port = models.IntegerField(blank=True, null=True)
    baud_rate = models.CharField(max_length=10, blank=True, null=True)
    data_bits = models.CharField(max_length=2, blank=True, null=True)
    parity = models.CharField(max_length=10, blank=True, null=True)
    stop_bits = models.CharField(max_length=4, blank=True, null=True)
    flow_control = models.CharField(max_length=20, blank=True, null=True)
    modem_port = models.CharField(max_length=10, blank=True, null=True)
    tel_no = models.CharField(max_length=15, blank=True, null=True)
    data_frequency = models.PositiveIntegerField(blank=True,null=True)
    week_day = models.PositiveIntegerField(blank=True, null=True)
    month_day = models.PositiveIntegerField(blank=True, null=True)
    #data_time = models.CharField(max_length=5)
    data_unit = models.SmallIntegerField(blank=True,null=True)
    dial_prefix = models.CharField(max_length=255,default=None)
    createdby = models.CharField(max_length=50, default=None)
    createddate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modifiedby = models.CharField(max_length=50, default=None)
    modifieddate = models.DateTimeField(auto_now=True, null=True, blank=True)
    smartmeter_logo = models.IntegerField(blank=True, null=True)
    device_type = models.IntegerField(blank=True,null=True)
    reading_type = models.CharField(max_length=7,default=None)
    #pcclient_id = models.IntegerField(blank=True,null=True)
    #contentright = models.CharField(max_length=1, blank=True, null=True)


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
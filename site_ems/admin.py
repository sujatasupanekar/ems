from django.contrib import admin
from .models import Company,Consortium,Location,Area
from .models import SmartmeterPort,Smartmeter,Brand_and_Manufacturer
from .models import Consumption05,Costarea,Provider,ProviderAllocation

# Register your models here.
class displayTimestamp(admin.ModelAdmin):
    disp = ('createddate','modifieddate')

admin.site.register(Area)
admin.site.register(Company,displayTimestamp)
admin.site.register(Consortium)
admin.site.register(Location)
admin.site.register(SmartmeterPort)
admin.site.register(Smartmeter)
admin.site.register(Brand_and_Manufacturer)
admin.site.register(Consumption05)
admin.site.register(Costarea)
admin.site.register(Provider)
admin.site.register(ProviderAllocation)
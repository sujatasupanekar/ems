from django.contrib import admin
from .models import Company,Consortium,Location,Area

# Register your models here.
class displayTimestamp(admin.ModelAdmin):
    disp = ('createddate','modifieddate')

admin.site.register(Area)
admin.site.register(Company,displayTimestamp)
admin.site.register(Consortium)
admin.site.register(Location)
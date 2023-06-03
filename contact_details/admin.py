from django.contrib import admin
from contact_details.models import ContactDetails
# Register your models here.

class contactDetailsAdmin(admin.ModelAdmin):
    list_display= ['id','name','email','subject','contact_number','message','created_at','updated_at']
admin.site.register(ContactDetails,contactDetailsAdmin)

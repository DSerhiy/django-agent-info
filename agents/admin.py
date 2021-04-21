from django.contrib import admin
from .models import Country, TimeZone, Port, Agent, ContactDetails, Email, AgentCargo, AgentVesselType


# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name', 'id')


class TimeZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class PortAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'time_zone')
    list_display_links = ('name',)
    search_fields = ('name', 'id')


class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'country_of_registry')
    list_display_links = ('name',)
    search_fields = ('name', 'id')


class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'agent', 'port', 'phone', 'main_email', 'website')
    list_display_links = ('id',)
    search_fields = ['port__name', 'agent__name']


class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_details', 'email')
    list_display_links = ('email',)
    search_fields = ('email',)


class AgentCargoAdmin(admin.ModelAdmin):
    list_display = ('id', )
    list_display_links = ('id',)
    search_fields = ('agent__name',)


class AgentVesselTypeAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('agent__name',)


admin.site.register(Country, CountryAdmin)
admin.site.register(TimeZone, TimeZoneAdmin)
admin.site.register(Port, PortAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(ContactDetails, ContactDetailsAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(AgentCargo, AgentCargoAdmin)
admin.site.register(AgentVesselType, AgentVesselTypeAdmin)

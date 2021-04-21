from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('json-country', get_country_list, name='json_country'),
    path('json-port/', get_port_list, name='json_port'),
    path('json-port/<int:country_id>', get_port_list, name='json_port'),
    path('json-agent/<int:port_id>', get_agent_list, name='json_agent'),

]
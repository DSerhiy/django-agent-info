from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import *

# Create your views here.


def index(request):
    return render(request, 'agents/index.html', {})


def get_country_list(request):
    country_list = Country.objects.all()
    country_list_json = [country.get_country_json() for country in country_list]

    return JsonResponse(country_list_json, safe=False)


def get_port_list(request, country_id=None):
    print(country_id)
    if country_id is None:
        port_list = Port.objects.all()
    else:
        port_list = Port.objects.filter(country__pk=country_id)
    port_list_json = [port.get_port_json() for port in port_list]
    return JsonResponse(port_list_json, safe=False)


def get_agent_list(request, port_id=None):
    print(port_id)
    if port_id is None:
        agent_list = []
    else:
        agent_list = ContactDetails.objects.filter(port__pk=port_id)
    agent_list_json = [agent.get_agent_json() for agent in agent_list]
    return JsonResponse(agent_list_json, safe=False)


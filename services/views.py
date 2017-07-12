from django.shortcuts import render
from models import Service
from django.core.context_processors import csrf





# Create your views here.
def all_services(request):
    services = Service.objects.all()
    context_dict = {}
    context_dict.update(csrf(request))
    return render(request, ('services.html', context_dict), {'services': services})



def services_detail(request, id):

    services = Service.objects.get(pk=id)
    context_dict = {}
    context_dict.update(csrf(request))

    return render(request, ('services_details.html', context_dict), {'services': services})


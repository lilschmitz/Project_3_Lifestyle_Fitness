from django.shortcuts import render
from services.models import Service
from django.template.context_processors import csrf





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

def successful_purchase(request):
    services = Service.objects.all()
    context_dict = {}
    context_dict.update(csrf(request))
    return render(request, ('successful_purchase.html', context_dict), {'services': services})
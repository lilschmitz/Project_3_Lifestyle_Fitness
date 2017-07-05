from django.shortcuts import render
from models import Service
from django.template.context_processors import csrf


# Create your views here.
def all_services(request):
    services = Service.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, "services.html", {"services": services}, args)

def services_detail(request, id):

    services = Service.objects.get(pk=id)
    args = {}
    args.update(csrf(request))
    return render(request, "services_details.html", {"services": services}, args)


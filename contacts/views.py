from django.shortcuts import render, get_object_or_404

from contacts.models import Contact


def index(request):

    return render(request, 'index.html')


def contact_list(request):

    contact_outline = Contact.objects.all()
    return render(request, "contacts.html", {'contacts': contact_outline})

def contact_detailed(request, id):

    contact_detail = get_object_or_404(Contact, pk=id)
    return render(request, "contact_details.html", {'contact': contact_detail})


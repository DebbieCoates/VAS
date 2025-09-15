from django.shortcuts import render, get_object_or_404 
from .models import Contact

# Homepage.
def home(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts })

def about(request):
    return render(request, 'about.html', {})    

#Individual contact page.
def contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'contact.html', {'contact': contact})
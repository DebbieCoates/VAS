from django.shortcuts import render
from .models import Contact

# Homepage.
def home(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts })

def about(request):
    return render(request, 'about.html', {})    
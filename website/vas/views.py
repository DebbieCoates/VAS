from django.shortcuts import render, get_object_or_404 , redirect
from .models import Contact
from django.contrib import  messages


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

#Delete a contact
def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    names =f"{contact.first_name} {contact.last_name}"
    contact.delete()
    messages.success(request, f'Contact "{names}" deleted successfully.')
    return redirect('home')


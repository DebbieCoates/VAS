from django.shortcuts import render, get_object_or_404 , redirect
from .models import Contact
from django.contrib import  messages
from .forms import UpdateContact


# Homepage.
def home(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts })

def about(request):
    return render(request, 'about.html', {})    

#Individual contact page.
def contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    form = UpdateContact(request.POST or None, request.FILES or None, instance=contact)
    if form.is_valid():
        form.save()
        messages.success(request, 'Contact updated successfully.')
        return redirect('home')
    else:
        return render(request, 'contact.html', {'contact': contact, 'form': form})  
    

#Delete a contact
def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    names =f"{contact.first_name} {contact.last_name}"
    contact.delete()
    messages.success(request, f'Contact "{names}" deleted successfully.')
    return redirect('home')


# Add A New Contact
def add_contact(request):
	form = UpdateContact(request.POST or None, request.FILES or None)
	# Check for filled out form
	if form.is_valid():
		# save the form
		saver = form.save(commit=False)
		# Add user ID to the form
		saver.user = request.user
		# Save the form for realz
		saver.save()	

		messages.success(request, "A New Contact Has Been Added!")
		return redirect('home')
	else:
		return render(request, 'add_contact.html', {"form":form})



from django.shortcuts import render, get_object_or_404 , redirect
from .models import Contact
from django.contrib import  messages
from .forms import UpdateContact
from django.contrib.auth import authenticate, login, logout 


#login
def login_user(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in!")
                return redirect('home')
            else:
                messages.error(request, "There was an error logging in. Please try again...")
                return redirect('login')    
        else:
            return render(request, 'login.html', {})

#logout
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

#register
def register_user(request):
    return render(request, 'register.html', {})


# Homepage.
def home(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.all()
        return render(request, 'home.html', {'contacts': contacts })
    else:
        return render(request, 'home.html', {})
    
# About page.
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



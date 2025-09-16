from django import forms
from .models import Contact

#Create an update form for Contact model
class UpdateContact(forms.ModelForm):

    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "First Name", 'class': 'form-control'}), max_length=100, required=False)
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Last Name", 'class': 'form-control'}), max_length=100, required=False)
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': "Email", 'class': 'form-control'}), max_length=100,required=False)
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Phone", 'class': 'form-control'}), max_length=20, required=False)
    address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Address 1", 'class': 'form-control'}), max_length=255, required=False)
    address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Address 2", 'class': 'form-control'}), max_length=100, required=False)
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "City", 'class': 'form-control'}), max_length=100, required=False)
    county = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "County", 'class': 'form-control'}), max_length=100, required=False)
    postcode = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Postcode", 'class': 'form-control'}), max_length=20, required=False)
    country = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Country", 'class': 'form-control'}), max_length=100, required=False)
    image = forms.ImageField(label="", widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False)
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'address1', 'address2', 'city', 'county', 'postcode', 'country', 'image']

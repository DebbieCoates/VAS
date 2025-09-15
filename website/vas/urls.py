
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/<int:id>', views.contact, name='contact'),
    path('delete/<int:id>', views.delete_contact, name='delete_contact'),
]

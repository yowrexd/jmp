from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .views import contact_submit, success_view, contact_list, contact_create, contact_delete, contact_detail

urlpatterns = [
    path('', views.reservation_form, name='reservation_form'),
    path('index/', views.index, name="index.html"),
    path('about/', views.about, name="about.html"),
    path('contact/', views.contact, name="contact.html"),
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('contacts/create/', contact_create, name='contact_create'),
    path('contacts/delete/<int:pk>/', contact_delete, name='contact_delete'),
    path('room/', views.room, name='room'),
    path('respage/', views.respage, name="reservations_page"),
    path('reservation/<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('reservation/<int:pk>/edit/', views.reservation_edit, name='reservation_edit'),
    path('reservation/<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logoutUser, name='logout'),
    path('admin-dashboard/', login_required(views.admin_dashboard), name='admin_dashboard'),
    path('contact-submit/', contact_submit, name='contact_submit'),
    path('success/', success_view, name='success'),
]

# Rest of your views and imports...

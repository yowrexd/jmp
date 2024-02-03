from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ReservationForm, ContactUsForm
from django.contrib import messages
from .models import *


def reservation_form(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_form')  # Redirect to a success page
    else:
        form = ReservationForm()

    return render(request, 'pages/index.html', {'form': form})

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')    

def room(request):
    return render(request, 'pages/room.html')

def respage(request):
    reservations = Reservation.objects.all()
    return render(request, 'pages/reservations_page.html', {'reservations': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'pages/reservation_detail.html', {'reservation': reservation})

def reservation_edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)

    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_detail', pk=reservation.pk)
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'pages/reservation_edit.html', {'form': form, 'reservation': reservation})

def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservations_page')  # Redirect to the reservations page after deletion

    return render(request, 'pages/reservation_delete.html', {'reservation': reservation})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'registration/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login_view')

@login_required
def admin_dashboard(request):
    reservations = Reservation.objects.all()
    return render(request, 'pages/admin_dashboard.html', {'reservations': reservations})


from django.http import HttpResponseRedirect
from .models import ContactUs
from django.urls import reverse

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Save data to the database using the ContactUs model
        entry = ContactUs(name=name, email=email, subject=subject, message=message)
        entry.save()

        # Redirect after successful submission
        return HttpResponseRedirect(reverse('success'))

    return render(request, 'contact_form.html')


def contact_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'pages/contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(ContactUs, pk=pk)
    return render(request, 'pages/contact_detail.html', {'contact': contact})

def contact_create(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactUsForm()

    return render(request, 'pages/contact_create.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(ContactUs, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')

    return render(request, 'pages/contact_delete.html', {'contact': contact})



def success_view(request):
    return render(request, 'pages/succes.html')
from django.shortcuts import render, redirect
from .forms import registrationform
from .models import Registration
from django.contrib import messages
from Register.autoemail import emailsent


def registration(request):
    cities = []
    form = registrationform()
    if request.method == "POST":
        form = registrationform(request.POST)
        if form.is_valid:
            state_selected = request.POST.get('stateselect')
            city_selected = request.POST.get('cityselect')
            name = request.POST.get('name')
            email = request.POST.get('email')
            # if Registration.objects.filter(email=email).exists():
            #     messages.info(request, "Email already Registered")
            # else:
            try:
                emailsent(name, email,state_selected,city_selected)
                Registration.objects.create(name=name,email=email,statename=state_selected,cityname=city_selected)
                form = registrationform()
                messages.success(request, f"Hii {name}, email for covid-19 data of your area is succesfully sent")
            except KeyError:
                messages.error(request, "District and State doesn't Match")
    return render(request, 'index.html', { 'form':form })


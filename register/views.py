from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User


# Create your views here.

def register(response):
    error = ""
    form = RegistrationForm()
    if response.method == "POST":
        username = response.POST.get("username")
        email = response.POST.get("email")
        print(response.POST)
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            for user in User.objects.all():
                if user.username == username:
                    error = "username"
                elif user.email == email:
                    error = "email"
                else:
                    error = "other"
            form = RegistrationForm()
            return render(response, "register/signup.html", {"error": error, "form": form})

    return render(response, "register/signup.html", {"form": form})

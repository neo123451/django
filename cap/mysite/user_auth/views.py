from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
def user_login(request):
    return render(request, 'authentication/Login.html')

def Home(request):
    return render(request, 'authentication/Home.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(reverse('user_auth:Login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('user_auth:show_user'))

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("user_auth:Home")
        messages.error(request, "Unsuccessful. Invalid information")
    form = NewUserForm()
    return render(request=request, template_name="authentication/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("user_auth:Home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="authentication/Login.html", context={"login_form":form})



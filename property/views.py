from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .forms import SignUpForm
from .forms import PropertyForm
from .models import Property

# Create your views here.
def index(request):
    print(request.user)
    properties = Property.objects.all()
    return render(request, 'index.html', {'propertys': properties})
    # return HttpResponse("this is homepage")

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')  # Redirect to a home page or other appropriate page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'signin.html')
    return render(request, 'signin.html')

def user_logout(request):
    logout(request)
    return redirect("/")

def about(request):
    return render(request, 'about.html') 

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/listing')  # Redirect to your desired URL
    else:
        form = PropertyForm()
    return render(request, 'AddProperty.html', {'form': form})


def contact(request):
    return render(request, 'contact.html') 

def property_listing(request):
    properties = Property.objects.all()  # Retrieves all products from the database
    return render(request, 'propertylist.html', {'propertys': properties})

def my_listing(request):
    properties = Property.objects.filter(user=request.user)  # Retrieves all products from the database
    return render(request, 'mylisting.html', {'propertys': properties})
 
    
# def contact(request):
#     # if request.method == "POST":
#     #     name = request.POST.get('name')
#     #     email = request.POST.get('email')
#     #     phone = request.POST.get('phone')
#     #     desc = request.POST.get('desc')
#     #     contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
#     #     contact.save()
#     #     messages.success(request, 'Your message has been sent!')
#     return render(request, 'contact.html')
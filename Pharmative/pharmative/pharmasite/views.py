from django.shortcuts import render, redirect
from django.http import HttpResponse
from pharmasite.models import Products
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, "index.html", context)



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email is exist ')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username,  password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                messages.info(request, 'User Create Successfully !!!')
                # print("success")
                return redirect('login_view')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:
        print("no post method")
        return render(request, 'register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_view')
    else:
        return render(request, 'login.html')







def products(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, "shop.html", context)


def selected_product(request, medicine_name):
    selected_product = Products.objects.get(slug=medicine_name)
    return render(request, "shop-single.html", {'selected_product': selected_product})


def search(request):
    product = request.GET['query']
    selected_product = Products.objects.get(name=product)
    return render(request, "shop-single.html", {'selected_product': selected_product})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def form_submission(request):
    c_fname = request.POST['c_fname']
    c_lname = request.POST['c_lname']
    c_email = request.POST['c_email']
    c_subject = request.POST['c_subject']
    c_message = request.POST['c_message']

    form = Form.objects.create(c_fname=c_fname, c_lname=c_lname, c_email=c_email, c_subject=c_subject, c_message=c_message)
    form.save()

    return render(request, "contact.html")

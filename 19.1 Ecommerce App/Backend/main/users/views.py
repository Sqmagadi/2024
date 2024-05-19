from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import UpdateUserForm, UpdateUserPassword, UpdateInfoForm, ShippingAddressForm
from django.contrib.auth.models import User
from store.models import Profile, ShippingAddress
import json
from cart.cart import Cart

def register_user(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home') 
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                #Shopping cart
            current_user = Profile.objects.get(user__id=request.user.id)
            # Get saved cart from the model
            saved_cart = current_user.old_cart
            if saved_cart:
                #Convert the string back  to dictionary using JSON
                converted_cart = json.loads(saved_cart)
                
                #Add to session
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

                messages.info(request, ('Login successful!'))
                return redirect('home')  
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!!!'))
    return redirect('home')


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UpdateInfoForm(request.POST or None, instance=current_user)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Your info has been updated"))
            return redirect('home')
        return render(request, 'core/update_info.html', {'form': form})
    else:
        messages.error(request, ("You must be logged in to update your info"))
    return render(request, 'core/update_info.html')


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = UpdateUserPassword(current_user ,request.POST) 
            
            if form.is_valid():
                form.save()
                messages.success(request, ("Your password has been updated. Login with your new password"))
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
                     
        else:
            form = UpdateUserPassword(current_user)
            return render(request, 'core/update_password.html', {'form': form})
    else:
        messages.error(request, ("You must be logged in to update your password"))
        return redirect('home')

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user) 
        
        if user_form.is_valid():
            user_form.save()
            
            login(request, current_user)
            messages.success(request, ("User Details updated"))
            return redirect('home')
        return render(request, 'core/update_user.html', {'user_form': user_form})
    else:
        messages.error(request, ("You must be logged in to update your details"))
        return redirect('home')


    return redirect('home')


def user_profile(request):
    return render(request, 'core/user_profile.html')

def shipping_info(request):
    if request.user.is_authenticated:
        current_user = ShippingAddress.objects.get(user__id=request.user.id)
        form = ShippingAddressForm(request.POST or None, instance=current_user)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Your info has been updated"))
            return redirect('home')
        return render(request, 'core/shipping_information.html', {'form': form})
    else:
        messages.error(request, ("You must be logged in to update your info"))
    return render(request, 'core/shipping_information.html')


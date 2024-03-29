from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages

from .forms import ProductForm


# Create your views here.
def dashboard(request):
    return render(request, 'crm/dashboard.html')

#register
def admin_signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    context = {'form': form}
    return render(request, 'crm/signup.html', context)
    
    
    

# User Login    
def admin_signin(request):
    if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None: 
                login(request, user)
                messages.success(request, ('Login sucess!'))
                return redirect('dashboard')
            else:
                messages.success(request, ('Error Logging in. Try again!!!'))
                return redirect('signin')
    else:
        return render(request, 'crm/signin.html')
    
# User Logout  
def admin_signout(request):
    logout(request)
    messages.success(request, ('You have been logged out!!!'))
    return redirect('signin')

@login_required
# Add product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return render(request, 'crm/add_product.html')
    else:
        form = ProductForm()
    return render(request, 'crm/add_product.html', {'form': form})
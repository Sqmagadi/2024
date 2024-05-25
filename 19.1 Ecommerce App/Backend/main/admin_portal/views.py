from pyexpat.errors import messages
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product, ProductImage
from .forms import ProductImageForm, ProductModelForm, CategoryModelForm

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.utils import timezone
from users.decorators import group_required


from django.contrib import messages


def admin_or_staff_required(view_func):
    # Decorator that checks if the user is an admin or staff member
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not (request.user.is_staff or request.user.is_superuser):
            return HttpResponse(status=401)  # Or redirect to login page or show a 401 error page
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@group_required('Admin')
def admin_portal(request):
    products = Product.objects.all()
    
    new_products = products.order_by('-created_at')[:10] 

    context = {
        'products':products,
        'new_products': new_products,
        
    }
    return render(request, 'admin_portal/admin_portal.html', context)

def add_product(request):
    products = Product.objects.all()
    products_count = products.count()
    new_products_count = products.filter(is_new=True).count()
    out_of_stock_count = products.filter(in_stock=False).count()
    is_listed_count = products.filter(is_listed=True).count()
    
    if request.method == 'POST':
        product_form = ProductModelForm(request.POST, request.FILES)
        product_image_form = ProductImageForm(request.POST, request.FILES)
        
        if product_form.is_valid() and product_image_form.is_valid():
            product = product_form.save()
            images = product_image_form.cleaned_data['product_images']
            for image in images:
                ProductImage.objects.create(product=product, product_images=image)
            
            messages.success(request, 'Product and images saved successfully!')
            return redirect('add_product')  # replace with your actual view name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        product_form = ProductModelForm()
        product_image_form = ProductImageForm()
    
    context = {
        'product_form': product_form,
        'product_image_form': product_image_form,
        'products': products,
        'products_count': products_count,
        'new_products_count': new_products_count,
        'out_of_stock_count': out_of_stock_count,
        'is_listed_count': is_listed_count,
    }
    
    return render(request, 'admin_portal/add_product.html', context)


@group_required('Admin')
def add_category(request):
    form = CategoryModelForm(request.POST)
    context = {
        'form': form
    }
    pass

# @admin_or_staff_required
@group_required('Admin')
def inventory(request):
    products = Product.objects.all()
    products_count = products.count()
    new_products_count = products.filter(is_new=True).count()
    out_of_stock_count = products.filter(in_stock=False).count()  
    is_listed_count = products.filter(is_listed=True).count()  
    context = {
        'products': products,
        'products_count': products_count,
        'new_products_count': new_products_count,
        'out_of_stock_count': out_of_stock_count,
        'is_listed_count': is_listed_count,
    }
    return render(request, 'admin_portal/inventory.html', context)


@group_required('Admin')
def product_inventory(request, pk):
    product = get_object_or_404(Product, id=pk)
    products = Product.objects.all()
    products_count = products.count()
    new_products_count = products.filter(is_new=True).count()
    out_of_stock_count = products.filter(in_stock=False).count()
    is_listed_count = products.filter(is_listed=True).count()

    if request.method == 'POST':
        product_form = ProductModelForm(request.POST, request.FILES, instance=product)
        product_image_form = ProductImageForm(request.POST, request.FILES)
        
        if product_form.is_valid() and product_image_form.is_valid():
            product_form.save()
            images = product_image_form.cleaned_data['product_images']
            for image in images:
                ProductImage.objects.create(product=product, product_images=image)
                
            messages.success(request, 'Product and images updated successfully!')
            return redirect('inventory')  # Replace 'inventory' with your actual inventory view name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        product_form = ProductModelForm(instance=product)
        product_image_form = ProductImageForm()

    context = {
        'product': product,
        'product_form': product_form,
        'product_image_form': product_image_form,
        'products_count': products_count,
        'new_products_count': new_products_count,
        'out_of_stock_count': out_of_stock_count,
        'is_listed_count': is_listed_count
    }
    return render(request, 'admin_portal/product_inventory.html', context)


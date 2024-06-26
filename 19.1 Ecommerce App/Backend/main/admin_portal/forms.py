from django import forms
from django.forms import ModelForm

from store.models import Category
from store.models import Product, ProductImage

# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True

# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)

#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = [single_file_clean(data, initial)]
#         return result
    
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        kwargs.setdefault("required", False) 
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        if not data and self.required:
            raise forms.ValidationError('This field is required.')
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter category name'
            }),
        }

class ProductModelForm(forms.ModelForm):
    new_category = forms.CharField(
    max_length=100, 
    required=False, 
    label="New Category",
    widget=forms.TextInput(attrs={'placeholder': 'Enter new category if not listed above. Leave blank if availlable.'})
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'description', 'image', 'is_sale', 'sale_price', 'in_stock', 'stock_quantity', 'is_new', 'is_featured', 'is_listed']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter product name'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter product price'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter product description',
                'rows': 8,
                'cols': 60
            }),
            'sale_price': forms.NumberInput(attrs={
                'placeholder': 'Enter sale price if applicable'
            }),
            'stock_quantity': forms.NumberInput(attrs={
                'placeholder': 'Enter stock quantity'
            }),
        }

    def save(self, commit=True):
        new_category_name = self.cleaned_data.get('new_category')
        if new_category_name:
            category, created = Category.objects.get_or_create(name=new_category_name)
            self.instance.category = category
        return super().save(commit=commit)

class ProductImageForm(forms.Form):
    product_images = MultipleFileField()

    def clean_product_images(self):
        images = self.files.getlist('product_images')
        if len(images) > 5:
            raise forms.ValidationError('You can upload a maximum of 5 images.')
        return images

        

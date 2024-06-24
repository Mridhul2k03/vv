from django import forms
from django.contrib.auth.models import User
from .models import CartModel, Footwearimages,Footwears,Footwearsize,OrderModel

class UserRegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'username','password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter Password'}),
            'first_name': forms.TextInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter Username'}),
            'email': forms.TextInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter Email'}),
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter Password'}),
            'username': forms.TextInput(attrs={'class':'form-control bg-transparent  p-2 my-2 regin','placeholder':'Enter Username'}),
        }

class CartForm(forms.ModelForm):

    class Meta: 
        model = CartModel
        fields = ['quantity',]
        widgets = {
            'quantity': forms.NumberInput(attrs={'class':'form-control w-25','placeholder':'','max':'5','min':'1'}),
        } 
        
        

class FootwearsForm(forms.ModelForm):
    class Meta:
        model = Footwears
        fields = '__all__'
        widgets={
            'product_category':forms.Select(attrs={'class':'form-select w-25 paddform'}),
            'product_types':forms.Select(attrs={'class':'form-select w-25 paddform'}),
            'product_name':forms.TextInput(attrs={'class':'form-control w-25 ','placeholder':'Footwear Name'}),
            'product_price': forms.NumberInput(attrs={'class': 'form-control w-25', 'placeholder': 'Product Price'}),
            'product_description':forms.Textarea(attrs={'class':'form-control paddform','placeholder':'enter the description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control w-25'}),
            'product_color':forms.Select(attrs={'class':'form-select w-25 paddform'}),
        }

class FootwearimagesForm(forms.ModelForm):
    class Meta:
        model = Footwearimages
        fields = ['product_image','product_color']
        widgets = {
            'product_image': forms.ClearableFileInput(attrs={'class': 'form-control w-50'}),
            'product_color':forms.Select(attrs={'class':'form-select w-50 paddform'}),
        }
        
class FootwearSizeForm(forms.ModelForm):
    class Meta:
        model = Footwearsize
        fields = ['size']
        widgets = {
            'size':forms.Select(attrs={'class':'form-select w-25 paddform'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['quantity','phone','email','address']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class':'form-control w-25','placeholder':'','max':5,'min':1}),
            'phone':forms.TextInput(attrs={'class':'form-control w-100','placeholder':'Enter your number','maxlength':10,'minlength':10}),
            'email':forms.EmailInput(attrs={'class':'form-control w-100','placeholder':'enter email'}),
            'address':forms.TextInput(attrs={'class':'form-control w-100','placeholder':'address'})
        }
class AdminOrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['status']
        widgets = {
            'status':forms.Select(attrs={'class':'form-select w-25 paddform'}),
        }
        
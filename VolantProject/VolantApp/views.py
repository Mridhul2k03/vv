from django.forms import BaseModelForm, ModelForm
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from .decorators import login_required
from .forms import AdminOrderForm, CartForm, FootwearimagesForm, FootwearsForm, OrderForm, UserRegisterForm,UserLoginForm,FootwearSizeForm
from django.views import View
from django.views.generic import TemplateView,CreateView,UpdateView,ListView,DeleteView,DetailView,FormView
from django.contrib.auth import login,logout,authenticate
from .models import Footwears,Footwearimages,CartModel,Footwearsize, OrderModel
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.db.models import Sum

# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'
    
class UserRegisterView(CreateView):
    template_name = 'user_reg.html'
    form_class = UserRegisterForm
    model = User
    
    def form_valid(self, form):
        User.objects.create_user(**form.cleaned_data)
        return redirect('landinghome')

class UserLogin(View):
    def get(self,request,*args, **kwargs):
        form=UserLoginForm()
        return render(request,'userlogin.html',{'form':form})
    
    def post(self,request,*args, **kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user.is_superuser:
            login(request,user)
            return redirect('adminpage')
        elif user:
            login(request,user)
            return render(request,'0userindex.html')
        else:
            form=UserLoginForm()
            return render(request,'userlogin.html',{'form':form})

class Userlogout(View):
    def get(self,request):
        logout(request)
        return redirect('landinghome')

class UserIndex(TemplateView):
    template_name = '0userindex.html'
    
class GentsProductsView(TemplateView):
    template_name = 'gentspro.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pro = Footwears.objects.filter(product_types='gents')
        context['products'] = pro
        return context
    
    
class LadiesProductsView(TemplateView):
    template_name = 'ladiespro.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pro = Footwears.objects.filter(product_types='ladies')
        context['products'] = pro
        return context
    
    
class GirlsBoysProductsView(TemplateView):
    template_name = 'boysgirlspro.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pro = Footwears.objects.filter(Q(product_types='girls') | Q(product_types='boys'))
        context['products'] = pro
        return context
    
    
    
    
class KidsProductsView(TemplateView):
    template_name = 'kidspro.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pro = Footwears.objects.filter(product_types='kids')
        context['products'] = pro
        return context
    
@method_decorator(login_required, name='dispatch')    
class UserGentsProductsView(TemplateView):
    template_name = '1loginedGentsPro.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pro = Footwears.objects.filter(product_types='gents')
        context['products'] = pro
        return context
    
@method_decorator(login_required, name='dispatch')    
class UserLadiesProductsView(TemplateView):
    template_name = '2.loginedLadiesPro.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pro = Footwears.objects.filter(product_types='ladies')
        context['products'] = pro
        return context
    
@method_decorator(login_required, name='dispatch')    
class UserGirlsBoysProductsView(TemplateView):
    template_name = '3loginedBGPro.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pro = Footwears.objects.filter(Q(product_types='girls') | Q(product_types='boys'))
        context['products'] = pro
        return context
    
    
    
@method_decorator(login_required, name='dispatch')    
class UserKidsProductsView(TemplateView):
    template_name = '4loginedKidsPro.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pro = Footwears.objects.filter(product_types='kids')
        context['products'] = pro
        return context
    

class ProductDetailView(DetailView):
    template_name = 'productview.html'
    model = Footwears
    context_object_name = 'products'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pro"] = Footwearimages.objects.filter(product_id = self.object.id)
        context["related"] = Footwears.objects.filter(product_types = self.object.product_types).exclude(id=self.object.id).order_by('-id')[:4]
        context['size'] = Footwearsize.objects.filter(product_id = self.object.id)
        
        return context
    

class AboutView(TemplateView):
    template_name = 'about.html'
    
class ConatctView(TemplateView):
    template_name = 'contact.html'
    
class TermsAndConditons(TemplateView):
    template_name = 'TandC.html'

class PrivacyPolicy(TemplateView):
    template_name = 'PP.html'

@method_decorator(login_required, name='dispatch')
class UserAboutView(TemplateView):
    template_name = '5userabout.html'

@method_decorator(login_required, name='dispatch')
class UserConatctView(TemplateView):
    template_name = '6usercontact.html'
    
@method_decorator(login_required, name='dispatch')    
class UserProductDetailView(DetailView):
    template_name = '7userproductview.html'
    model = Footwears
    context_object_name = 'products'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pro"] = Footwearimages.objects.filter(product_id = self.object.id)
        context["related"] = Footwears.objects.filter(product_types = self.object.product_types).exclude(id=self.object.id).order_by('-id')[:4]
        context['size'] = Footwearsize.objects.filter(product_id = self.object.id)
        return context
    
@method_decorator(login_required, name='dispatch')    
class CartListView(ListView):
    template_name = '9cartlist.html'
    model = CartModel
    context_object_name = 'products'
    
    def get_queryset(self):
        return CartModel.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_sum = CartModel.objects.filter(user=self.request.user).aggregate(total=Sum('total'))['total']
        # Ensure total_sum is not None
        context["sum"] = total_sum if total_sum is not None else 0
        return context
    

@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        product = Footwears.objects.get(id=id)
        color = Footwearimages.objects.filter(product_id=id)
        size = Footwearsize.objects.filter(product_id=id)
        form = CartForm()
        return render(request, '8addticart.html',{'form': form, 'product': product, 'color': color, 'size': size})
    
    def post(self, request, *args, **kwargs):
        user = request.user
        id = kwargs.get('id')
        product = Footwears.objects.get(id=id)
        color_id = request.POST['product_color']
        size_id = request.POST['size']
        
        color = Footwearimages.objects.get(id=color_id)
        size = Footwearsize.objects.get(id=size_id)
        
        quantity = request.POST.get('quantity')
        total = product.product_price * int(quantity)
        
        print(color_id, size_id, color, size, quantity, total)
        
        if user.is_authenticated:
            CartModel.objects.create(user=user, product=product, color=color, size=size, quantity=int(quantity), total=total)
            return redirect('user_index')
        else:
            return redirect('login')
        

@method_decorator(login_required, name='dispatch')
class BuyNowView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        product = Footwears.objects.get(id=id)
        color = Footwearimages.objects.filter(product_id=id)
        size = Footwearsize.objects.filter(product_id=id)
        form = OrderForm()
        return render(request, '10buyingpagre.html',{'form': form, 'product': product, 'color': color, 'size': size})
    
    def post(self, request, *args, **kwargs):
        user = request.user
        id = kwargs.get('id')
        product = Footwears.objects.get(id=id)
        color_id = request.POST['product_color']
        size_id = request.POST['size']
        
        color = Footwearimages.objects.get(id=color_id)
        size = Footwearsize.objects.get(id=size_id)
        
        quantity = request.POST.get('quantity')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        total = product.product_price * int(quantity)
        
        print(color_id, size_id, color, size, quantity, total)
        
        if user.is_authenticated:
            OrderModel.objects.create(user=user, product=product, color=color, size=size, quantity=int(quantity), total=total, phone = phone, email = email, address = address )
            return redirect('user_index')
        else:
            return redirect('login')
        
@method_decorator(login_required, name='dispatch')        
class RemoveCartItem(View):
    def get(self,request,*args, **kwargs):
        id = kwargs.get('id')
        item = CartModel.objects.get(id=id)
        item.delete()
        return redirect('user_index')

@method_decorator(login_required, name='dispatch')
class UserOrderView(ListView):
    template_name = '11userorder.html'
    model = OrderModel
    context_object_name = 'products'
    
    def get_queryset(self):
        return OrderModel.objects.filter(user=self.request.user)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_sum = OrderModel.objects.filter(user=self.request.user).aggregate(total=Sum('total'))['total']
        # Ensure total_sum is not None
        context["sum"] = total_sum if total_sum is not None else 0
        return context
    
    
 # _________________Admin views starts_____________________________________
    
    
@method_decorator(login_required, name='dispatch')
class AdminIndexView(TemplateView):
    template_name = 'AdminPage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.all()
        context['user'] = user
        return context

@method_decorator(login_required, name='dispatch')
class AdminProductListView(ListView):
    template_name = 'adminproducts.html'
    model = Footwears
    context_object_name = 'products'
    
    def get_queryset(self):
        return Footwears.objects.all()

@method_decorator(login_required, name='dispatch')   
class AdminAddProductView(CreateView):
    template_name = 'adminproductadd.html'
    model = Footwears
    form_class = FootwearsForm
    
    def form_valid(self, form):
        Footwears.objects.create(**form.cleaned_data)
        return redirect('adminproducts')

@method_decorator(login_required, name='dispatch')
class AdminUpdateProductView(UpdateView):
    template_name = 'adminproductupdate.html'
    model = Footwears
    form_class = FootwearsForm
    context_object_name = 'product'
    pk_url_kwarg = 'id'
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('adminproducts')

@method_decorator(login_required, name='dispatch')
class AdminAddimage(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        product = Footwears.objects.get(id = id)
        image = Footwearimages.objects.filter(product_id = id)
        form = FootwearimagesForm()
        return render(request, 'adminaddimage.html', {'form': form, 'product': product, 'image': image})
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        product = Footwears.objects.get(id=id)
        image = request.FILES.get('product_image')
        color = request.POST.get('product_color')
        if Footwearimages.objects.filter(product_id = id, product_color=color).exists():
            return redirect('adminproducts')
        else:
            Footwearimages.objects.create(product = product, image=image, product_color=color)
            return redirect('adminproducts')
    
@method_decorator(login_required, name='dispatch')
class AdminAddSize(View):   
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')   
        product = Footwears.objects.get(id=id)
        form = FootwearSizeForm()
        sizes = Footwearsize.objects.filter(product_id = id)
        return render(request, 'adminaddsize.html', {'form': form, 'product': product, 'sizes': sizes})
    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        product = Footwears.objects.get(id=id)
        size = request.POST.get('size')
        if Footwearsize.objects.filter(product_id=id, size=size).exists():
            return redirect('adminproducts')
        else:
            Footwearsize.objects.create(product=product, size=size)
            return redirect('adminproducts')

@method_decorator(login_required, name='dispatch')
class AdminDeleteProductView(View):    
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        product = Footwears.objects.get(id=id)
        product.delete()
        return redirect('adminproducts')
        
class AdminOrderList(ListView):
    template_name = 'adminorders.html'
    model = OrderModel
    context_object_name = 'orders'
    
    def get_queryset(self):
        return OrderModel.objects.all().exclude(status = 'delivered')
    


@method_decorator(login_required, name='dispatch')
class AdminOrdersDetail(DetailView):
    template_name = 'adminorderdetail.html'
    model = OrderModel
    context_object_name = 'order'
    pk_url_kwarg = 'id'

@method_decorator(login_required, name='dispatch')
class AdminUpdateOrderView(UpdateView):
    template_name = 'adminorderupdate.html'
    model = OrderModel
    form_class = AdminOrderForm
    context_object_name = 'order'
    pk_url_kwarg = 'id'
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('adminorderlist')
    
    
# __________________________Admin Views end_______________________________ 
"""
URL configuration for VolantProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from VolantApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='landinghome'),
    path('userregister/',views.UserRegisterView.as_view(),name='user_register'),
    path('userlogin',views.UserLogin.as_view(),name='user_login'),
    path("userlogout",views.Userlogout.as_view(), name="logout"),
    path('index/',views.UserIndex.as_view(),name='user_index'),
    path('gentsview/',views.GentsProductsView.as_view(),name='gentsview'),
    path('ladiesview/',views.LadiesProductsView.as_view(),name='ladiesview'),
    path('bgview/',views.GirlsBoysProductsView.as_view(),name='bgview'),
    path('kidsview/',views.KidsProductsView.as_view(),name='kidsview'),
    path('usergentsview/',views.UserGentsProductsView.as_view(),name='usergentsview'),
    path('userladiesview/',views.UserLadiesProductsView.as_view(),name='userladiesview'),
    path('userbgview/',views.UserGirlsBoysProductsView.as_view(),name='userbgview'),
    path('userkidsview/',views.UserKidsProductsView.as_view(),name='userkidsview'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact/',views.ConatctView.as_view(),name='contact'),
    path('userabout/',views.UserAboutView.as_view(),name='userabout'),
    path('usercontact/',views.UserConatctView.as_view(),name='usercontact'),
    path("terms/", views.TermsAndConditons.as_view(), name="terms"),
    path("privacy/", views.PrivacyPolicy.as_view(), name="privacy"),
    path('detail/<int:id>',views.ProductDetailView.as_view(),name='detail'),
    path('userdetail/<int:id>',views.UserProductDetailView.as_view(),name='userdetail'),
    path('addtocart/<int:id>',views.AddToCartView.as_view(),name='addtocart'),
    path('list/',views.CartListView.as_view(),name='list'),
    path('adminpage/',views.AdminIndexView.as_view(),name='adminpage'),
    path('adminproducts/',views.AdminProductListView.as_view(),name='adminproducts'),
    path('addpro/',views.AdminAddProductView.as_view(),name='add_pro'),
    path('update/<int:id>',views.AdminUpdateProductView.as_view(),name='update_pro'),
    path('image/<int:id>',views.AdminAddimage.as_view(),name='image'),
    path('size/<int:id>',views.AdminAddSize.as_view(),name='size'),
    path('cart/remove/<int:id>',views.RemoveCartItem.as_view(),name='cart_remove'),
    path('buy/<int:id>',views.BuyNowView.as_view(),name='buy_view'),
    path('adminorderlist/',views.AdminOrderList.as_view(),name='adminorderlist'),
    path('adminordersdetail/<int:id>',views.AdminOrdersDetail.as_view(),name='adminordersDetail'),
    path('adminorderupdate/<int:id>',views.AdminUpdateOrderView.as_view(),name='adminorderupdate'),
    path('admindelepeproduct/<int:id>',views.AdminDeleteProductView.as_view(),name='admindelepeproduct'),
    path('userorderlist',views.UserOrderView.as_view(),name='userorderlist'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

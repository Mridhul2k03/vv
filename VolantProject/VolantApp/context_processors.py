from .models import CartModel

def cart_count(request):
    if request.user.is_authenticated:
        return {'cart_count':CartModel.objects.filter(user=request.user,status='in_cart').count()}
    else:
        return {'cart_count':0}
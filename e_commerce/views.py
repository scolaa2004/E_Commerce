from django.shortcuts import render , get_object_or_404
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})




from django.shortcuts import redirect

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = [(product, cart[str(product.id)]) for product in products]
    return render(request, 'store/cart.html', {'cart_items': cart_items})




from django.shortcuts import redirect
from .models import Order

def checkout(request):
    cart = request.session.get('cart', {})
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        order = Order(user=request.user, product=product, quantity=quantity)
        order.save()
    request.session['cart'] = {}  # Clear the cart after checkout
    return redirect('order_confirmation')

def order_confirmation(request):
    return render(request, 'store/order_confirmation.html')


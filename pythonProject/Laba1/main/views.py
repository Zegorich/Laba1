from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import RegisterForm, NewProduct
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

def index(request):
    products = Product.objects.all()
    if request.method == "POST":
        messages.success(request, f"{products.name} added to your cart.")
        return redirect("main:add_to_cart", product_name=products.name)
    return render(request, 'main/index.html', {'products': products})

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

class register_view(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("main:profile")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

@login_required
def add_to_cart(request, product_name):
    cart_item = Cart.objects.filter(user=request.user, product=product_name).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")
    else:
        Cart.objects.create(user=request.user, product=product_name)
        messages.success(request, "Item added to your cart.")

    return redirect("main:cart_detail")

@login_required
def remove_from_cart(request, product_name):
    cart_item = get_object_or_404(Cart, product=product_name)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("main:cart_detail")

@login_required
def cart_detail(request):

    cart_items = Cart.objects.filter(user=request.user)
    print(cart_items)
    for item in cart_items:
        item.price = Product.objects.get(name=item.product).price
        item.QP = item.quantity * item.price
    total_price = sum(item.quantity * item.price for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart/cart_detail.html", context)

@login_required
def orders(request):
    user = request.user
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        order = Order()
        order.user = user
        order.product = item.product
        order.quantity = item.quantity
        order.price = Product.objects.get(name=item.product).price
        order.save()
        remove_from_cart(request, item.product)


    return render(request, "cart/cart_detail.html")

@permission_required(perm='main.view_order2', raise_exception=True)
def orders_detail(request):

    all_orders = Order.objects.filter()
    user = User.objects.filter()
    user_details = Order2.objects.filter()
    Order2.objects.all().delete()
    for u in user:
        user_ = Order2()
        user_.user = u
        user_.spent_money = 0
        user_.account_money = 0
        user_.credit_limit = 1
        user_.current_debt = 1
        user_.credit_remains = 1
        user_.save()

    for user_ in user_details:
        for item in all_orders:
            if user_.user == item.user:
                user_.spent_money += item.price

    context = {
        "user_details": user_details,
    }
    return render(request, "orders/orders_detail.html", context)

def add_new_item(request):
    if request.method == "POST":
        form = NewProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form = NewProduct()

    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})

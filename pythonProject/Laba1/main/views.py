from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegisterForm


from django.shortcuts import render, redirect, get_object_or_404
from .models import *


from django.contrib import messages

def index(request):
    products = Product.objects.all()
    if request.method == "POST":
        messages.success(request, f"{products.name} added to your cart.")
        return redirect("main:add_to_cart", product_id=products.id)
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
def add_to_cart(request, product_id):
    cart_item = Cart.objects.filter(user=request.user, product=product_id).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Item added to your cart.")
    else:
        Cart.objects.create(user=request.user, product=product_id)
        messages.success(request, "Item added to your cart.")

    return redirect("main:cart_detail")

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("main:cart_detail")

@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * Product.objects.get(id=item.product).price for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "products": Product.objects.all(),
    }

    return render(request, "cart/cart_detail.html", context)


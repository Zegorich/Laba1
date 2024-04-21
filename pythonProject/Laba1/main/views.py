from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegisterForm

from .models import Product

from django.shortcuts import render, get_object_or_404
from .models import Product



def index(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})




@login_required
def profile_view(request):
    return render(request, 'main/profile.html')


class register_view(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("profile")


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, available=True)
    return render(request, 'cart/templates/cart/cart.html', {'product': product})
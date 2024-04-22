from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegisterForm


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
    success_url = reverse_lazy("main:profile")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


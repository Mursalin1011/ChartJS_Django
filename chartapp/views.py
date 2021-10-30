from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm

# Create your views here.

def index(request):

    products = Products.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()

    context = {
        "products": products,
        "form": form,
    }

    return render(request, 'chartapp/index.html', context)
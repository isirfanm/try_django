from django.http import HttpRequest
from django.shortcuts import render

from .models import Product
from .forms import ProductForm


# Create your views here.
def product_create_view(request: HttpRequest):
    context = {}
    return render(request, "products/product_create.html", context)


# def product_create_view(request: HttpRequest):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get("title")
#         print(my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

# def product_create_view(request: HttpRequest):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {"form": form}
#     return render(request, "products/product_create.html", context)


def product_detail_view(request):
    product = Product.objects.get(id=1)
    # context = {"title": product.title, "description": product.description}
    context = {"product": product}
    return render(request, "products/product_detail.html", context)

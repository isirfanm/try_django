from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm


# Create your views here.
def render_initial_data(request):
    initial_data = {"title": "My default title"}
    obj = Product.objects.get(id=1)
    # form = ProductForm(request.POST or None, initial=initial_data)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {"form": form}
    return render(request, "products/product_create.html", context)


def dynamic_lookup_view(request, id):
    # product = Product.objects.get(id=id)
    # product = get_object_or_404(Product, id=id)
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {"product": product}
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        # confirming delete
        product.delete()
        return redirect("../../")
    context = {"product": product}
    return render(request, "products/product_delete.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {"object_list": queryset}
    return render(request, "products/product_list.html", context)


# def product_create_view(request: HttpRequest):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


# def product_create_view(request: HttpRequest):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#         my_new_title = request.POST.get("title")
#         print(my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)


def product_create_view(request: HttpRequest):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/product_create.html", context)


def product_detail_view(request):
    product = Product.objects.first()
    # context = {"title": product.title, "description": product.description}
    context = {"product": product}
    return render(request, "products/product_detail.html", context)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ProductCategory, Product

# Create your views here.
def index(request):
    return HttpResponse("Products index")

def product_category_detail(request, prod_cat_id):
    # try:
    #   prod_cat = ProductCategory.objects.get(pk=prod_cat_id)
    # except ProductCategory.DoesNotExist:
    #   return Http404("Product Category does not exist")
    # return HttpResponse(prod_cat)
    prod_cat = get_object_or_404(ProductCategory, pk=prod_cat_id)
    return render(request=request,
                  template_name='product_category/detail.html',
                  context={'title': 'Product Category',
                           'prod_cat': prod_cat})

def product_category_list(request, prod_cat):
    return HttpResponse(prod_cat)

def product_detail(request, prod_id):
    return HttpResponse(prod_id)

def product_list(request, prod):
    return HttpResponse(prod)

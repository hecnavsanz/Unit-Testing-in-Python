from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
    prods = prod_cat.product_set.all().order_by('prod_name')
    pager = Paginator(prods, 4)
    page_num = request.GET.get('page')
    page_prod = pager.get_page(page_num)
    return render(request=request,
                  template_name='product_category/detail.html',
                  context={'title': 'Product Category',
                           'prod_cat': prod_cat,
                           'prods': page_prod})


def product_category_list(request):
    prod_cats = ProductCategory.objects.all().order_by('prod_cat_name')
    pager = Paginator(prod_cats, 4)
    page_num = request.GET.get('page')
    page_prod_cats = pager.get_page(page_num)
    return render(request=request,
                  template_name='product_category/list.html',
                  context={'title': 'Product Categories',
                           'prod_cats': page_prod_cats})


def product_category_create(request):
    if request.method == 'POST':
        prod_cat = ProductCategory(prod_cat_name=request.POST['prod_cat_name'],
                                   prod_cat_code=request.POST['prod_cat_code'])
        prod_cat.save()
        return HttpResponseRedirect(reverse('product_category_list'))
    else:
        return render(request=request,
                      template_name='product_category/add.html',
                      context={'title': 'Product Category Create'})


def product_category_update(request, prod_cat_id):
    prod_cat = get_object_or_404(ProductCategory, pk=prod_cat_id)
    # update product category
    if request.method == 'POST':
        prod_cat.prod_cat_name = request.POST['prod_cat_name']
        prod_cat.prod_cat_code = request.POST['prod_cat_code']
        prod_cat.save()

    return render(request=request,
                  template_name='product_category/edit.html',
                  context={'title': 'Product Category Edit',
                           'prod_cat': prod_cat})


def product_category_delete(request, prod_cat_id):
    prod_cat = get_object_or_404(ProductCategory, pk=prod_cat_id)
    prod_cat.delete()
    return HttpResponseRedirect(reverse('product_category_list'))


def product_list(request):
    prods = Product.objects.all().order_by('prod_name')
    prod_cats = ProductCategory.objects.all()
    pager = Paginator(prods, 4)
    page_num = request.GET.get('page')
    page_prod = pager.get_page(page_num)
    return render(request=request,
                  template_name='product/list.html',
                  context={'title': 'Products List',
                           'prods': page_prod,
                           'prod_cats': prod_cats})


def product_create(request):
    if request.method == 'POST':
        prod_cat = ProductCategory.objects.get(pk=request.POST['prod_cat_id'])
        prod = Product(prod_name=request.POST['prod_name'],
                       prod_status=request.POST['prod_status'],
                       prod_price=request.POST['prod_price'],
                       prod_count=request.POST['prod_count'],
                       prod_cat_id=prod_cat, )
        prod.save()
        return HttpResponseRedirect(reverse('product_list'))
    else:
        prod_cats = ProductCategory.objects.all().order_by("prod_cat_name")
        return render(request=request,
                      template_name='product/add.html',
                      context={'title': 'Product Add',
                               'prod_cats': prod_cats})


def product_update(request, prod_id):
    prod = get_object_or_404(Product, pk=prod_id)
    # update product
    if request.method == 'POST':
        prod.prod_name = request.POST['prod_name']
        prod.prod_status = request.POST['prod_status']
        prod.prod_price = request.POST['prod_price']
        prod.prod_count = request.POST['prod_count']
        prod.prod_cat_id = ProductCategory.objects.get(pk=request.POST['prod_cat_id'])
        prod.save()
        return HttpResponseRedirect(reverse('product_list'))
    else:
        prod_cats = ProductCategory.objects.all()
        return render(request=request,
                      template_name='product/edit.html',
                      context={'title': 'Product Edit',
                               'prod': prod,
                               'prod_cats': prod_cats})


def product_delete(request, prod_id):
    prod = get_object_or_404(Product, pk=prod_id)
    prod.delete()
    return HttpResponseRedirect(reverse('product_list'))

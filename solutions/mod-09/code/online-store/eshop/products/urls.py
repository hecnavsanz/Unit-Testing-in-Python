from django.urls import path
from . import views


urlpatterns = [
  path("", views.index, name="index"),
  path("product_category/<int:prod_cat_id>/", views.product_category_detail, name="product_category_detail"),
  path("product_category/<int:prod_cat_id>/edit/", views.product_category_update, name="product_category_update"),
  path("product_category/<int:prod_cat_id>/delete/", views.product_category_delete, name="product_category_delete"),
  path("product_category/add/", views.product_category_create, name="product_category_create"),
  path("product_category/list", views.product_category_list, name="product_category_list"),
  path("product/list", views.product_list, name="product_list"),
  path("product/<int:prod_id>/edit/", views.product_update, name="product_update"),
  path("product/<int:prod_id>/delete/", views.product_delete, name="product_delete"),
  path("product/add/", views.product_create, name="product_create"),
]

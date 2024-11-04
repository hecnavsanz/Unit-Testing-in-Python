from django.urls import path
from . import views


urlpatterns = [
  path("", views.index, name="index"),
  path("product_category/<int:prod_cat_id>/", views.product_category_detail, name="product_category_detail"),
  path("product_categories/", views.product_category_list, name="product_category_list"),
  path("product/<int:prod_cat_id>/", views.product_detail, name="product_detail"),
  path("products/", views.product_list, name="product_list"),
]

import json
from django.db import models
from django.db.models import CharField


class ProductCategory(models.Model):
    # product categories
    class Categories(models.TextChoices):
        TELEVISION = 'TV'
        MONITOR = 'MO'
        DISPLAY = 'DI'

    # prod_cat_id = models.IntegerField(name='prod_cat_id', primary_key=True, auto_created=True)
    prod_cat_id = models.AutoField(name='prod_cat_id', primary_key=True)
    prod_cat_name = models.CharField(name='prod_cat_name', max_length=50)
    prod_cat_code = models.CharField(name='prod_cat_code', max_length=2, choices=Categories, default=Categories.DISPLAY)

    # product string
    def __str__(self) -> CharField:
        return self.prod_cat_name

    # product category json string
    def to_json(self) -> str:
        return json.dumps({'prod_cat_id': str(self.prod_cat_id),
                           'prod_cat_name': self.prod_cat_name,
                           'prod_cat_code': self.prod_cat_code})


class Product(models.Model):
    # product status
    class Status(models.IntegerChoices):
        ACTIVE = 1
        INACTIVE = 0

    prod_id = models.AutoField(name='prod_id', primary_key=True)
    prod_name = models.CharField(name='prod_name', unique=True, max_length=100)
    prod_cat_id = models.ForeignKey(name='prod_cat_id', blank=False, null=False,
                                    to=ProductCategory, to_field='prod_cat_id',
                                    on_delete=models.CASCADE)
    prod_status = models.IntegerField(name='prod_status', choices=Status)
    prod_price = models.DecimalField(name='prod_price', max_digits=5, decimal_places=2)
    prod_count = models.IntegerField(name='prod_count', blank=False, null=False, default=0)

    # product string
    def __str__(self) -> CharField:
        return self.prod_name

    # product json string
    def to_json(self) -> str:
        return json.dumps({'prod_id': str(self.prod_id),
                           'prod_name': self.prod_name,
                           'prod_cat_id': self.prod_cat_id,
                           'prod_status': self.prod_status,
                           'prod_price': self.prod_price,
                           'prod_count': self.prod_count})

    # product inventory total
    def prod_inv_total(self):
        return round(self.prod_count * self.prod_price, 2)

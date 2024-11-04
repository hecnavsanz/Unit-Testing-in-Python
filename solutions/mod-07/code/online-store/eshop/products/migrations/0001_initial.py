# Generated by Django 5.1.2 on 2024-11-01 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('prod_cat_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('prod_cat_name', models.CharField(max_length=50)),
                ('prod_cat_code', models.CharField(choices=[('TV', 'Television'), ('MO', 'Monitor'), ('DI', 'Display')], default='DI', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=100, unique=True)),
                ('prod_status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')])),
                ('prod_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('prod_count', models.IntegerField(default=0)),
                ('prod_cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory')),
            ],
        ),
    ]

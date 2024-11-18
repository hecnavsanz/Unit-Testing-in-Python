from http.cookiejar import debug

from behave import given, when, then
import psycopg2


@given(u'the user is on the Product Category page')
def the_user_is_on_the_product_category_page(context):
    response = context.test_client.get('/products/product_category/list')

    assert response.status_code == 200
    assert b'<title>eShop Application - Product Categories</title>' in response.content


@given('the user has entered the product category with name {name} and code {code}')
def the_user_has_entered_a_product_category(context, name, code):
    # this emulates entering the product category name and code
    context.name = name
    context.code = code
    assert 1 == 1


@when('the user clicks on the Add button')
def the_user_clicks_on_the_add_button(context):
    # this emulates the click on the add button
    context.test_client.post('/products/product_category/add/',
                             {"prod_cat_name": context.name, "prod_cat_code": context.code})
    assert 1 == 1


@then('the product category with name {name} and code {code} is added')
def the_product_category_should_be_added(context, name, code):
    with psycopg2.connect(host='localhost', port=9090, dbname='test_eshop_db', user='postgres', password='Pytest-TDD.Labs_4ALL') as conn:
        with conn.cursor() as cursor:
            query = f"SELECT prod_cat_name, prod_cat_code FROM products_productcategory WHERE prod_cat_name = '{context.name}' AND prod_cat_code = '{context.code}'"
            cursor.execute(query)
            prod_cat = cursor.fetchone()
            assert prod_cat[0] == context.name
            assert prod_cat[1] == context.code


@then('the product category ({name}, {code}) is displayed the Product Category list page')
def the_user_is_redirected_to_the_product_category_list_page(context, name, code):
    response = context.test_client.get('/products/product_category/list')

    assert response.status_code == 200
    assert b'<td>' + name.encode() + b'</td>' in response.content
    assert b'<td>' + code.encode() + b'</td>' in response.content

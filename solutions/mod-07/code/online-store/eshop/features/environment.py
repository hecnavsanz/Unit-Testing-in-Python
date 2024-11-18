from behave import use_fixture
from online_store_fixtures import django_test_runner, django_test_case, django_test_client

# set this env var before calling behave features/product_category.feature
# to configure the django settings for behave tests
# export DJANGO_SETTINGS_MODULE=features.behave_settings


def before_all(context):
    use_fixture(django_test_runner, context)


def before_scenario(context, scenario):
    use_fixture(django_test_case, context)
    use_fixture(django_test_client, context)

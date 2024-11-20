from behave import fixture
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase
from django.test import Client
import django


@fixture
def django_test_runner(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    # context.test_database = context.test_runner.setup_databases()
    yield
    # context.test_runner.teardown_databases(context.test_database)
    context.test_runner.teardown_test_environment()


@fixture
def django_test_case(context):
    context.test_case = LiveServerTestCase
    context.test_case.setUpClass()
    yield
    context.test_case.tearDownClass()
    del context.test_case


@fixture
def django_test_client(context):
    context.test_client = Client()
    yield
    del context.test_client

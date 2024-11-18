# File: test_sales_employee_status.py
import pytest
from pytest_bdd import scenario, given, when, then
from datetime import datetime, time
from sales_employee import SalesEmployee


@pytest.fixture
def a_sales_employee():
    return SalesEmployee('John Doe', 'john.doe@labs.io')


@pytest.fixture
def a_datetime():
    return datetime(2023, 6, 14, 10, 30)


@scenario('office_hours.feature', 'Offline Status')
def test_offline_status():
    pass


@given('a sales employee')
def test_valid_sales_employee(a_sales_employee):
    assert a_sales_employee is not None
    assert a_sales_employee.get_type() == 'sales'


@when('the time and date is not at office hours')
def test_datetime_not_at_office_hours(a_datetime):
    current_time = a_datetime.time()
    current_date = a_datetime.date()
    assert (current_date.weekday() in range(0, 4) and
            (current_time < time(9, 0) or current_time > time(18, 0))) or \
           (current_date.weekday() in range(5, 6))


@then(u'the employee status is offline')
def test_employee_status_offline(a_sales_employee, a_datetime):
    assert a_sales_employee.is_online(a_datetime) is False

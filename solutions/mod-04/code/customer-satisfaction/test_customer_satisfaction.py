import pytest
from pytest_bdd import given, scenario, then, when
from survey import Survey
from customer import Customer

@pytest.fixture
def customer():
    return Customer('John Doe', 'john.doe@labs.io')

@pytest.fixture
def survey(customer):
    survey = Survey(customer)
    survey.add_answer(4)
    survey.add_answer(4)
    survey.add_answer(6)
    survey.set_status('completed')
    return survey


@scenario('customer_satisfaction.feature', 'Survey CSAT')
def test_survey_csat(survey):
    assert survey is not None


@given('the customer completed the survey')
def test_survey_status(survey):
    assert survey.get_status() == 'completed'


@when('the CSAT is below the 50%')
def test_survey_csat_lt_50_pct(survey):
    assert survey.compute_csat_score() < 50


@then('send a promotion code to the customer')
def test_send_promo_code(customer):
    assert customer.send_promo_code() == 'Promo code sent'

from pytest_bdd import scenarios, given, when, then
from app import app

# Load scenarios from the .feature file
scenarios('frontend/auth/login.feature')


# Define Given steps
@given('the user has entered valid login credentials', target_fixture='valid_credentials')
def valid_credentials():
    return '{"email": "labs", "password": "Pytest.Labs_4ALL"}'


# Define When steps
@when('the user clicks on the login button', target_fixture='click_login_button')
def click_login_button(valid_credentials):
    with app.test_client() as client:
        response = client.post('/login', data=valid_credentials)
    return response


# Define Then steps
@then('display the successful validation message')
def check_success_message(click_login_button):
    assert b'Successful login' in click_login_button.data

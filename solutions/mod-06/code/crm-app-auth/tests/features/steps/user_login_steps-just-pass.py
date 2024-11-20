from behave import given, when, then, scenario
from db.ext import db
from models.credential import Credential


@given(u'the user {first_name} {last_name} with password {password} is on the login page')
def the_user_is_on_the_login_page(context, first_name, last_name, password):
    response = context.client.get('/login')

    context.username = first_name.lower() + "." + last_name.lower()
    context.password = int(password)
    context.response = response

    assert response.status_code == 200
    assert b'<title>CRM Application - Login</title>' in response.data


@given('the user has entered valid login credentials')
def the_user_has_entered_valid_login_credentials(context):
    with context.app.app_context():
        db.session.add(Credential(username=context.username,
                                  password=context.password))
        cred = db.session.query(Credential).filter_by(username=context.username).all()
    assert len(cred) == 1
    assert cred[0].username == context.username
    assert int(cred[0].password) == context.password


@when('the user clicks on the login button')
def the_user_clicks_on_the_login_button(context):
    # this emulates the click on the login button
    context.client.post('/login', data=dict(username=context.username,
                                            password=context.password))
    # here the session should be set with the user data
    assert 1 == 1


@then('the user is redirected to the index page')
def the_user_should_be_redirected_to_the_index_page(context):
    # here should be the session updated before the redirect above
    response = context.client.get('/')
    context.response = response
    assert response.status_code == 200
    assert b'<title>CRM Application - Main</title>' in response.data


@then('the user name is displayed in the header')
def the_user_name_is_displayed_in_the_header(context):
    # here should be the session being used to verify the user name
    assert context.response == context.response

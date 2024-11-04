# tests/test_message_uppercase_fail.py
from pytest_bdd import scenario, given, then
from message_fail import to_uppercase


@scenario('message_processing.feature', 'Convert a message to uppercase')
def test_message_uppercase():
    pass

@given('a message', target_fixture='a_message')
def a_message():
    return 'Hello'

@then('return the message in uppercase')
def the_message_is_uppercase(a_message):
    expected_message = 'HELLO'
    assert to_uppercase(a_message) == expected_message

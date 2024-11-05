from pytest_bdd import scenario, given, then
from message import to_uppercase


@scenario('message_processing.feature', 'Convert a message to uppercase')
def test_message_uppercase():
    pass

@given('a message', target_fixture='a_message')
def a_message():
    return 'Pytest TDD and BDD together!'

@then('return the message in uppercase')
def the_message_is_uppercase(a_message):
    expected_message = 'PYTEST TDD AND BDD TOGETHER!'
    assert to_uppercase(a_message) == expected_message
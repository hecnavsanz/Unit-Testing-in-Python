# python -m behave --no-capture --no-capture-stderr .\features\create-event.feature

import time
from behave import given, when, then
from selenium.webdriver.common.by import By


@given(u'the user is on the Home page')
def go_to_home_page(context):
    context.driver.get("http://localhost:10080/web-apps/events-modular/index.html")
    context.driver.set_window_size(1200, 1200)
    assert context.driver.title == 'Events Application'

@given(u'the user clicks on the Create Event menu option')
def user_click_create_event(context):
    time.sleep(4) # element not interactable
    context.driver.find_element(By.ID, "navbarDropdown").click()
    context.driver.find_element(By.LINK_TEXT, "Create Event").click()
    assert context.driver.title == 'Create Event'

@given(u'the user enters the event data: {description}, {state}, {type} and {date}')
def user_enters_event_data(context, description, state, type, date):
    context.driver.find_element(By.NAME, "ce-description").click()
    context.driver.find_element(By.NAME, "ce-description").send_keys(description)
    if state == 'inactive':
        context.driver.find_element(By.ID, "ce-active-check").click()
    if type == 'private':
        context.driver.find_element(By.ID, "private").click()
    # context.driver.find_element(By.NAME, "ce-date").click()
    # context.driver.find_element(By.CSS_SELECTOR, ".datepicker-days .next").click()
    # context.driver.find_element(
    #     By.CSS_SELECTOR, "tr:nth-child(4) > .day:nth-child(6)"
    # ).click()
    context.driver.find_element(By.NAME, "ce-date").send_keys(date)

    if state == "active":
        v_state = True
    else:
        v_state = False

    assert context.driver.find_element(By.NAME, "ce-description").text in description
    assert context.driver.find_element(By.ID, "ce-active-check").is_selected() is v_state
    assert context.driver.find_element(By.ID, "private").is_selected() is ( True if type in "private" else False )
    assert context.driver.find_element(By.NAME, "ce-date").text in date


@when(u'the user clicks on the Submit button to create the event')
def user_click_submit_event(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    assert context.driver.title == 'List Events'


@then(u'the event data popup window is displayed: {description}, {state}, {type} and {date}')
def event_popup_data_displayed(context, description, state, type, date):
    time.sleep(6) # element not interactable
    context.driver.find_element(By.CSS_SELECTOR, "#eventModal .btn").click()
    pass

@then(u'the event data ({description}, {state}, {type} and {date}) is listed in the Event List')
def event_data_listed(context, description, state, type, date):
    context.driver.find_element(By.ID, "navbarDropdown").click()
    context.driver.find_element(By.LINK_TEXT, "List Events").click()
    context.driver.find_element(By.CSS_SELECTOR, ".btn-sm").click()
    time.sleep(10) # element not interactable
    context.driver.find_element(By.ID, "confirmDeleteBtn").click()
    time.sleep(4) # element not interactable
    context.driver.find_element(By.LINK_TEXT, "Home").click()
    time.sleep(4)
    pass

Feature: User Registration
  As a new user
  I want to register on the website
  So I can access to my account and start purchasing items

  Scenario: Successful registration
    Given the user is in the registration page
    When the user fills in valid registration details
    And clicks the "Register" button
    Then the user sees a success message
    And receives a confirmation email

Feature: User Login

  Scenario: Successful login
    Given the user has entered valid login credentials
    When the user clicks on the login button
    Then display the successful validation message

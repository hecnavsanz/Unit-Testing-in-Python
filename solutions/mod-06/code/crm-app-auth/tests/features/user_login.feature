Feature: User Login

  # behave --tags="@login" tests/features/user_login.feature
  @login
  Scenario Outline: Successful login
    Given the user <first_name> <last_name> with password <password> is on the login page
    And the user has entered valid login credentials
    When the user clicks on the login button
    Then the user is redirected to the index page
    And the user name is displayed in the header

    Examples: Users
      | first_name | last_name | password |
      | Nick       | Danger    | 123456   |
      | Ann        | Risk      | 654321   |

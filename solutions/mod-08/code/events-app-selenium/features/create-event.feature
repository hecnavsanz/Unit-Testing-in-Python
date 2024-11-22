Feature: Events

  Scenario Outline: Create Event
    Given the user is on the Home page
    And the user clicks on the Create Event menu option
    And the user enters the event data: <description>, <state>, <type> and <date>
    When the user clicks on the Submit button to create the event
    Then the event data popup window is displayed: <description>, <state>, <type> and <date>
    And the event data (<description>, <state>, <type> and <date>) is listed in the Event List

    Examples: Events
      | description    | state     | type    | date       |
      | Taylor Swing   | active    | private | 11/13/2024 |
      | Jackie Tong    | inactive  | public  | 12/05/2024 |

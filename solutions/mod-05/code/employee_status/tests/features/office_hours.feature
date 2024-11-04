# File: office_hours.feature
Feature: Office Hours
    As an employee
    based on my office hours
    I want to appear offline or online

    Scenario: Offline Status
        Given a sales employee
        When the time and date is not at office hours
        Then the employee status is offline

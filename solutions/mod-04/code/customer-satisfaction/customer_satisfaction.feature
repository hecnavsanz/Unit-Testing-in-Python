Feature: Customer Satisfaction

    Scenario: Survey CSAT
        Given the customer completed the survey
        When the CSAT is below the 50%
        Then send a promotion code to the customer

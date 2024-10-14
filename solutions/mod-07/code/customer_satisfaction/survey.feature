Feature: Customer Satisfaction

    Scenario: Survey CSAT
        Given the customer purchased a product
        And received a survey by email
        And completed the survey
        When the customer csat is below the 50%
        Then send a promotion code by email

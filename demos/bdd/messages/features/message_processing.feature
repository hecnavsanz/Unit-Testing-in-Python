# features/message_uppercase.feature

Feature: Processing messages

  Scenario: Convert a message to uppercase
    Given a message
    Then return the message in uppercase

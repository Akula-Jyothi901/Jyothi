Feature: Basic Calculator Operations
    @basic_test
    Scenario: Add of two numbers
        Given the calculator is clear
        When enter 56 and 10 and press add
        Then the result should be 66

    Scenario: Subtract of two numbers
        Given the calculator is clear
        When enter 56 and 10 and press subtract
        Then the result should be 46

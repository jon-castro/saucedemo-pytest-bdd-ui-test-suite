@functional
@sorting
Feature: Saucedemo web page sorting functionality verification

    As a user,
    I want to use the Saucedemo web application sorting features,
    So that I can verify their functionality.

    Scenario: Sorting products by price, high to low is working.
        Given I log in with the standard user.
        When I sort products by price, high to low.
        Then the first price is higher than the second price.
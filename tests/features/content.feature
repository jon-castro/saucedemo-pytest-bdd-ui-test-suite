@content
@trivial
Feature: Saucedemo web page content verification

    As a user,
    I want to visit the Saucedemo web application pages,
    So that I can verify that all application content is present.

    Scenario: All Login page content is present.
        Given I am on the login page.
        Then all login page content is present.

    Scenario: All Header component content is present.
        Given I log in with the standard user.
        Then all header component content is present.

    Scenario: All Home page content is present.
        Given I log in with the standard user.
        Then all home page content is present.

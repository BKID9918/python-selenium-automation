
Feature: Tests for Target Search functionality

  Scenario: User can search for a product
    Given Open target main page
    When  Search for a product
    Then  Verify that correct search results shown

  Scenario: User can select cart
    Given Open target main page
    When  Click on Cart icon
    Then  Verify “Your cart is empty” message

  Scenario: User sign in
    Given Open target main page
    When  Click Sign In
    When  Click Sign In form navigation menu
    Then  Verify Sign In form opened



#    Then Verify that correct search results shown

#  Scenario: User can see Cart Empty message
#    Given Open target main page
#    When Click on cart icon
#    Then Verify cart Empty message shown
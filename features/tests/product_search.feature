Feature: Test Scenarios for Search functionality

#  Scenario: User can search for a product
#    Given Open Google page
#    When Input Car into search field
#    And Click on search icon
#    Then Product results for Car are shown

#  Scenario: open the Target Circle page
#    Given Open Target Circle page
#    Then Verify 10 benefit cells

Scenario Outline: User can search item in cart
  Given Open target main page
  When Search for <product>
  When Add <product> to cart
  Then Verify <product> in cart

  Examples:
  | product       |
  | paper towels  |
  | paper plates  |
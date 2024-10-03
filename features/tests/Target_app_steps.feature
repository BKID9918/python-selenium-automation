Feature: Tests for Target App page

#  Scenario: User is able to open Privacy Policy
#    Given Open Target App page
#    And Store original window
#    When Click Privacy Policy link
#    And Switch to new window
#    Then Verify Privacy Policy page opened
#    And Close current page
#    And Return to original window


    Scenario:User can open and enter invalid credentials
     Given Open Target App page
     When  Click on Sign In
     When  Click Sign In on navigation menu
     When  Click on Email or mobile phone
     And   Enter email jddd12@gmail.com
     When  Click on Password field
     And   Enter password this14u!1
     When  Click Sign in with password
     Then  Verify We can't find your account
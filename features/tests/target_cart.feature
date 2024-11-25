Feature: Test for clicks on the cart

  Scenario: User click on the cart icon
    Given Open target main page
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown
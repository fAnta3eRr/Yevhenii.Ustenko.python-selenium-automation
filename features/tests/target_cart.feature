Feature: Test for clicks on the cart

  Scenario: User click on the cart icon
    Given Open target main page
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown

  Scenario: User add a product to cart
    Given Open target main page
    When Search for tide
    And Click add to cart button
    And Add product name
    And Confirm Add to Cart from side Navigation
    And Open Cart Page
    Then Verify cart has at list 1 item(s)
    And Verify cart has correct product
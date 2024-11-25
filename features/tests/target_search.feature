# Created by yevheniiustenko at 11/23/24

  Feature: Tests for search

  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search results shown


  Feature: Test for clicks on the cart

  Scenario User click on the cart icon
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown


  Feature: Test navigate to Sign in form

  Scenario User can navigate to Sign in
    When Click Sign in
    Then From right side navigation menu, click Sign in
    Then Verify Sign in from opened


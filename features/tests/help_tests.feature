
Feature: Tests for Help pages

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened

  Scenario: User can select Help topic Target Circle
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened

  Scenario: User able select Gift Cards topic Target Help page
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Gift Cards
    Then Verify help Target GiftCard balance page opened

    #Extra HomeWork #4

  Scenario: User can see UI elements on the help page
      Given Open Target help page
      Then  Verify these 6 UI elements are present in a low box

  Scenario: User can see UI elements on the help page
      Given Open Target help page
      Then  Verify these 6 UI elements are present in a tall box

  Scenario: User can see UI elements on the help page
      Given Open Target help page
      Then  Verify these 5 UI elements are present in a right box
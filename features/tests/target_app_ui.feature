Feature: Tests for Target App page

  @smoke
  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window

  @smoke
  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    And Store original window
    Then Click on Target terms and conditions link
    Then Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original



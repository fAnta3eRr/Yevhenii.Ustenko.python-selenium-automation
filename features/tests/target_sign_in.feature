Feature: Test navigate to Sign in form

  Scenario: User can navigate to Sign in
    Given Open target main page
    When Click Sign in
    Then From right side navigation menu, click Sign in
    Then Verify Sign in from opened
Feature: Test navigate to Sign in form

  @smoke
  Scenario: User can navigate to Sign in
    Given Open target main page
    When Click Sign in
    Then From right side navigation menu, click Sign in
    Then Verify Sign in from opened

  @smoke
  Scenario: User can login using valid credentials
    Given Open target main page
    When Click Sign in
    Then From right side navigation menu, click Sign in
    And Input olgatimanovska13@gmail.com and Timanovska1308 on SignIn page
    And Click Sign in button
    Then Verify user is logged in (sign in form should disappear)

  Scenario: User can login using incorrect credentials
    Given Open target main page
    When Click Sign in
    Then From right side navigation menu, click Sign in
    And Input incorrect credentials olgatimanovska@gmail and 12345678 combination
    And Click Sign in button
    Then Verifies that Please enter a valid email or phone number message is shown
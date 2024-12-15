Feature: Tests for search

  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search result shown for tea

  Scenario: User can search for a product
    Given Open target main page
    When Search for forks
    Then Verify search result shown for forks

  Scenario: User can search for a product
    Given Open target main page
    When Search for tide
    Then Verify search result shown for tide


  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search result shown for <product>
    Examples:
    | product  |
    | tea      |
    | forks    |
    | tide     |




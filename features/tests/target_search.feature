Feature: Tests for search

  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search result shown for tea
    Then Verify search term tea in URl

  Scenario: User can search for a product
    Given Open target main page
    When Search for forks
    Then Verify search result shown for forks

  Scenario: User can search for a product
    Given Open target main page
    When Search for tide
    Then Verify search result shown for tide

  @smoke
  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search result shown for <product>
    Examples:
    | product  |
    | tea      |
    | forks    |
    | tide     |

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image

  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown








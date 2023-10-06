
Feature: Three Number Sum

  Scenario: Find triplets that sum up to target
    Given an array of numbers [12, 3, 1, 2, -6, 5, -8, 6]
    And a target sum of 0
    When I perform the three number sum
    Then I should get the triplets [-8, 2, 6], [-8, 3, 5], [-6, 1, 5]

  Scenario: No triplets found for target sum
    Given an array of numbers [1, 2, 3]
    And a target sum of 100
    When I perform the three number sum
    Then I should get an empty array []

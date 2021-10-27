Feature: US_0006 Compare cars
  As a future driver
  I wish I could compare two cars
  In order to know which one is the best

  Scenario: Kevin wants to buy a car and wants to know which one is faster
    Given Two cars already built
    When Kevin compares the two cars
    Then The system displays the fastest car
Feature: US_0011 Kebab order
  As a Kebab lover
  I want to place an order in a Kebab Truck
  In order to have a good time with my Kebab

  Scenario: Edward want to see the menu
    Given A kebab truck with menu
    When Edouard ask for the menu
    Then he should see the menu

  Scenario: Edward successfully orders a Kebab
    Given A kebab truck
    When Edouard place an order
    Then Edouard can see all his orders

  Scenario: Edward orders a Kebab with failure
    Given A kebab truck
    When Edouard place a bad order
    Then The system indicates an error

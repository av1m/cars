Feature: US_0010 Bidirectional Wheel
  As a pilot
  I want to know which cars are attached wheels
  In order to have a better view of my pieces

  Scenario: Thierry wants to add a wheel to a car
    Given An existing car and an existing wheel
    When Thierry adds wheels to this car
    Then The wheel appears in the car
    And The car is associated with the wheel

  Scenario: Thierry associates a car with a wheel
    Given An existing car and an existing wheel
    When Thierry associate a car to a wheel
    Then The wheel appears in the car
    And The car is associated with the wheel
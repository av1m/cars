Feature: US_0007 Weight of car
  As a driver
  I want to know the weight of my car
  In order to see if i ever have a chance to raise it to the hall

  Scenario Outline: Benjamin want to add a weight to his car
    Given A car already built with a weight
    When Benjamin change the <weight> to his car
    Then the <weight> of the car is increased

    Examples:
      | weight |
      | 1000   |
      | 500    |
      | 2300   |


  Scenario Outline: Benjamin want to create a car with a wrong weight
    Given Benjamin create a car with a <weight>
    When Benjamin change the <weight> to his car
    Then The system indicates an error

    Examples:
      | weight |
      | 0      |
      | -1     |
      | None   |

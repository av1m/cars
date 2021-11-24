Feature: US_0000 Car creation
  As a driver,
  I want to construct a new car with specific options of my choice
  So that I can drive it

  Scenario Outline: Benjamin creates his new car with success
    Given Nothing
    When Benjamin wants to create a car with a max speed <max_speed> and a number of horsepower <horsepower> and 10 size <number_of_wheels> wheels
    Then the car is created

    Examples:
      | max_speed | horsepower | number_of_wheels |
      | 100       | 100        | 2                |
      | 0         | 100        | 2                |
      | 100       | 1          | 0                |
      | 100       | 500        | 3                |
      | 20        | 30         | 4                |

  Scenario Outline: Because of wrong options, Benjamin can't construct his car
    Given Nothing
    When Benjamin initialise his car with options max speed <max_speed> and horsepower <horsepower>
    Then an error message is displayed indicate that an option is invalid

    Examples:
      | max_speed | horsepower |  |
      | -100      | 100        |  |
      | 100       | - 100      |  |
      | 100       | 100        |  |
      | 100       | 500        |  |




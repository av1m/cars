Feature:  US_0001 Car information
  As a driver with a car,
  I want to know specifications of my car
  So that I can be informed of it

  Scenario Outline:  Benjamin wants to know information about his car and success
    Given Benjamin initialise his car with parameters <max_speed>, <horsepower>
    When Benjamin asked information about his car
    Then information's car are displayed on screen

    Examples:
      | max_speed | horsepower |
      | 100       | 100        |
      | 0         | 100        |
      | 100       | 0          |
      | 100       | 500        |
      | 1         | 40         |
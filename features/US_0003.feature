Feature:  US_0003 Car wheel
  As a driver with a racing car,
  I want to add some wheels with size
  So that I can have enough to drift

  Scenario Outline: Benjamin wants to use his car in racing
    Given Benjamin had a racing car
    When he want to add <number_wheels> wheel of <wheel_size> size
    Then the system show us the newly wheels

    Examples:
      | number_wheels | wheel_size |
      | 4             | 100        |
      | 3             | 100        |
      | 2             | 20         |
      | 1             | 10         |
      | 9             | 1          |
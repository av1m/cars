Feature: US_0005 Color a car
  As a driver
  I want to add a color to my car
  So that my car becomes beautiful in my eyes

  Scenario Outline: Benjamin wants to be able to choose the color on his car
    Given A Colorless Car
    When Benjamin adds a <color>
    Then the car has the requested color

    Examples:
      | color   |
      | #232310 |
      | #FFFFFF |
      | #FF5733 |
      | #40E0D0 |
      | #008080 |

  Scenario Outline: Benjamin adds a color that is not available
    Given A Colorless Car
    When Benjamin adds a bad <color>
    Then a message indicates that the color is wrong

    Examples:
      | color   |
      | red     |
      | blue    |
      | #HELLO  |
      | #8989FG |
      | #4SE0D0 |
      | #008P80 |





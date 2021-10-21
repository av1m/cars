# Created benyamin at 10/5/21
Feature: US_0000 Car creation
  As a user,
  I want to create my car with parameters of my choice
  So that I can drive it

  Scenario Outline: Benjamin creates his new car with success
    Given None
    When Benjamin initialise his car with parameters <max_speed>, <horse_power>, and <wheels_list>
    Then the car is created

    Examples:
      | max_speed | horse_power | wheels_list                       |  |
      | 100       | 100         | None                              |  |
      | 0         | 100         | None                              |  |
      | 100       | 0           | None                              |  |
      | 100       | 500         | [(10, True),(10,True),(15,False)] |  |
      | None      | None        | None                              |  |

  Scenario Outline: Because of wrong parameters, Benjamin doesn't success to creates a car
    Given None
    When Benjamin initialise his car with parameters <max_speed>, <horse_power>, and <wheels_list>
    Then an error message is displayed

    Examples:
      | max_speed | horse_power | wheels_list                        |  |
      | -100      | 100         | None                               |  |
      | 100       | - 100       | None                               |  |
      | 100       | 100         | 0                                  |  |
      | 100       | 500         | [(-10, True),(-10,True),(15,False) |  |




# Created by benya at 21/10/2021
Feature:  US_0001 Car information
    As a user with a car,
    I want to know specifications of my car
    So that I can be informed of it

  Scenario Outline:  Benjamin wants to know information about his car and success
    Given Benjamin initialise his car with parameters <max_speed>, <horse_power>, and <wheels_list>
    When Benjamin asked information about his car
    Then car informations are displayed on screen

    Examples:
      | max_speed | horse_power | wheels_list                       |  |
      | 100       | 100         | None                              |  |
      | 0         | 100         | None                              |  |
      | 100       | 0           | None                              |  |
      | 100       | 500         | [(10, True),(10,True),(15,False)] |  |
      | None      | None        | None                              |  |
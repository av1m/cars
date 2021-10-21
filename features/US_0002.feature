# Created by benya at 21/10/2021
Feature: US_0002 Car modification
  As a user
  I want to modify the specifications of my car
  So that I can improve it

  Scenario Outline: Benjamin wants to improve the horse power and the max speed of his car and success
    Given Benjamin initialise his car with parameters <max_speed>, <horse_power>, and <wheels_list>
    When Benjamin asked to improve his car with <NewMax_speed> and <NewHorse_power>
    Then his car characteristics have been modified

    Examples:
      | max_speed | horse_power | wheels_list                       | NewMax_speed | NewHorse_power |  |
      | 100       | 100         | None                              | 200          | 200            |  |
      | 0         | 100         | None                              | 100          | 0              |  |
      | 100       | 0           | None                              | 300          | 300            |  |
      | 100       | 500         | [(10, True),(10,True),(15,False)] | 300          | 300            |  |

  Scenario Outline: Because of impossible value, Benjamin doesn't success to improve his car
    Given Benjamin has already defined his car with <max_speed> and <horse_power>
    When Benjamin asked to improve the characteristics up to <NewMax_speed> and <NewHorse_power>
    Then an error message is displayed

    Examples:
      | max_speed | horse_power | wheels_list                       | NewMax_speed | NewHorse_power |  |
      | 100       | 100         | None                              | -200         | -200           |  |
      | 0         | 100         | None                              | -100         | 0              |  |
      | 100       | 0           | None                              | 300          | None           |  |
      | 100       | 500         | [(10, True),(10,True),(15,False)] | None         | 300            |  |

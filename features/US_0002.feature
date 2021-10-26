Feature: US_0002 Car modification
  As a user
  I want to modify the specifications of my car
  So that I can improve it

  Scenario Outline: Benjamin wants to improve the horse power and the max speed of his car and success
    Given Benjamin has already defined his car with <max_speed> and <horse_power>
    When Benjamin asked to improve his car with <new_max_speed> and <new_horse_power>
    Then his car characteristics have been modified

    Examples:
      | max_speed | horse_power | new_max_speed | new_horse_power |
      | 100       | 100         | 200           | 200             |
      | 0         | 100         | 100           | 0               |
      | 100       | 0           | 300           | 300             |
      | 100       | 500         | 300           | 300             |

  Scenario Outline: Because of impossible value, Benjamin doesn't success to improve his car
    Given Benjamin has already defined his car with <max_speed> and <horse_power>
    When Benjamin asked to improve the characteristics up to <new_max_speed> and <new_horse_power>
    Then an error message is displayed

    Examples:
      | max_speed | horse_power | new_max_speed | new_horse_power |
      | 100       | 100         | -200          | -200            |
      | 0         | 100         | -100          | 0               |
      | 100       | 0           | 300           | None            |
      | 100       | 500         | None          | 300             |

Feature: US_0009 Compare Motor
  As a technician
  I want to compare two motors
  In order to see which is the better motor

  Scenario: Tony check which motor is the best
    Given Two motors already installed
    When I compare the two motors
    Then I should see the motor with the best performance
Feature: US_0008 Car compliant
  As a technician
  I want to know if the motor complies with the maximum speed
  In order to see the cars that may have problems over time

  Scenario: Tony checks a compliant car
    Given A car already built
    When Tony checks if the motor is compliant
    Then The system indicates the compliance

  Scenario: Tony checks a non-compliant car
    Given A car already built
    When Tony checks if the motor is compliant
    Then The system indicates an error

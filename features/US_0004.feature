Feature: US_0004 Max speed
  As a pilot,
  I wish to have an electric motor and be able to run my car at a certain speed
  So that I can feel the vibrations of the electric motor ...

  Scenario Outline: Thierry wants to use an electric car and build it to the maximum of these capacities
    Given An electric formula 1
    When Thierry improves the car so that it can go up to <kmh>
    Then Thierry can use an electric formula 1 climbed to its maximum speed

    Examples:
      | kmh |
      | 100 |
      | 100 |
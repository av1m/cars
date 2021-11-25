Feature: US_0012 Undo an order
  As a Kebab hater
  I want to undo an order in a Kebab Truck
  In order to have meanness to the cook

  Scenario: Hatward successfully cancel an order
    Given An order placed in a kebab truck
    When Hatward undo the last order
    Then the order is cancelled

  Scenario: Hatward try to cancel an order that was not placed
    Given A kebab truck
    When Hatward undo the last order that was not placed
    Then The system indicates an error

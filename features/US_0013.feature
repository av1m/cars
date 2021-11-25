Feature: US_0013 Favorite formula
  As a food lover
  I want to create a formula with my best food
  In order to have a list with all my favorite food

  Scenario Outline: Mister Patate want to create a formula with his best food
    Given Mister Patate's favorite foods (a <food> is represented by a <sauce> and <price>)
    And Mister Patate's favorite drink (Coca-Cola)
    When Mister Patate add food in his formula
    Then he should have a list with all his favorite foods

    Examples:
      | food  | sauce    | price |
      | Pizza | Tomato   | 5     |
      | Kebab | Barbecue | 5     |

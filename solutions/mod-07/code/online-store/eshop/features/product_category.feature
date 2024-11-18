Feature: Product Category

  Scenario Outline: Add Product Category
    Given the user is on the Product Category page
    And the user has entered the product category with name <name> and code <code>
    When the user clicks on the Add button
    Then the product category with name <name> and code <code> is added
    And the product category (<name>, <code>) is displayed the Product Category list page

    Examples: Product Categories
      | name    | code |
      | Tablet  | TB   |
      | Display | DI   |
      | Monitor | MO   |

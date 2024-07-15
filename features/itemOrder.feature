Feature: Amazon ItemOrder
  Scenario: Successful Item Order
    Given user on home page amazon
    When user enter itemname in search box
    And find searched item
    And store item price
    And click on Add to Cart Button
    And click on Go to Cart
    Then verify price on cart page
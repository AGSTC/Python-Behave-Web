Feature: Amazon Login
  Scenario: Successful user login
    Given user on sign in page amazon
    When user enter username
    And user click on continue
    And user enter password
    And click on Sign-In
    Then verify username on home page
    And close browser
Feature: SauceDemo E-Commerce End-to-End Suite
  As a standard user of SauceDemo
  I want to authenticate and complete a product checkout
  So that I can verify order placement functionality

  Background:
    Given user navigates to the SauceDemo login page

  @smoke @regression
  Scenario: Successful login with valid credentials
    When user logs in with username "standard_user" and password "secret_sauce"
    Then the user should see the product inventory page title as "Products"

  @negative
  Scenario: Locked out user receives error message
    When user logs in with username "locked_out_user" and password "secret_sauce"
    Then an error message should display "Sorry, this user has been locked out."

  @e2e
  Scenario: End-to-End product purchase flow
    When user logs in with username "standard_user" and password "secret_sauce"
    And user sorts products by "Price (high to low)"
    And user adds the first product to the cart
    And user proceeds to checkout with details "Tanay", "Tester", "411001"
    Then the order should be placed with confirmation "Thank you for your order!"
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Feature फाईल लोड करणे
scenarios("../features/saucedemo.feature")

@pytest.fixture
def context_data():
    return {}

@given("user navigates to the SauceDemo login page")
def navigate_to_login(page: Page, context_data):
    login_page = LoginPage(page)
    login_page.navigate()
    context_data["login_page"] = login_page
    context_data["inventory_page"] = InventoryPage(page)

@when(parsers.parse('user logs in with username "{username}" and password "{password}"'))
def step_login(context_data, username, password):
    context_data["login_page"].login(username, password)

@then(parsers.parse('the user should see the product inventory page title as "{title_text}"'))
def verify_inventory_title(context_data, title_text):
    expect(context_data["inventory_page"].title).to_have_text(title_text)

@then(parsers.parse('an error message should display "{error_text}"'))
def verify_error_message(context_data, error_text):
    error_loc = context_data["login_page"].get_error_message()
    expect(error_loc).to_contain_text(error_text)

@when(parsers.parse('user sorts products by "{sort_option}"'))
def sort_products(context_data, sort_option):
    context_data["inventory_page"].sort_products_high_to_low()

@when("user adds the first product to the cart")
def add_product(context_data):
    context_data["inventory_page"].add_first_product_to_cart()

@when(parsers.parse('user proceeds to checkout with details "{first_name}", "{last_name}", "{zip_code}"'))
def checkout_flow(page: Page, first_name, last_name, zip_code):
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()
    page.locator("#first-name").fill(first_name)
    page.locator("#last-name").fill(last_name)
    page.locator("#postal-code").fill(zip_code)
    page.locator("#continue").click()
    page.locator("#finish").click()

@then(parsers.parse('the order should be placed with confirmation "{confirmation_msg}"'))
def verify_order_success(page: Page, confirmation_msg):
    complete_header = page.locator(".complete-header")
    expect(complete_header).to_have_text(confirmation_msg)
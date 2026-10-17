import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# ----------------------------------------------------
# 🟢 TEST 1: Positive Login Test
# ----------------------------------------------------
def test_successful_login(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(inventory_page.title).to_be_visible()
    expect(inventory_page.title).to_have_text("Products")
    print("\n[PASS] Test 1: Login Successful")


# ----------------------------------------------------
# 🔴 TEST 2: Negative Login Test
# ----------------------------------------------------
def test_negative_login_locked_user(page: Page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")
    error_loc = login_page.get_error_message()
    expect(error_loc).to_be_visible()
    expect(error_loc).to_contain_text("Sorry, this user has been locked out.")
    print("\n[PASS] Test 2: LOCK user assertion completed")


# ----------------------------------------------------
# 🛒 TEST 3: End-to-End Purchase Flow
# ----------------------------------------------------
def test_e2e_product_checkout(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.sort_products_high_to_low()
    inventory_page.add_first_product_to_cart()
    inventory_page.verify_cart_count("1")

    page.locator(".shopping_cart_link").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    page.locator("#checkout").click()
    page.locator("#first-name").fill("Tanay")
    page.locator("#last-name").fill("Tester")
    page.locator("#postal-code").fill("411001")
    page.locator("#continue").click()

    page.locator("#finish").click()
    complete_header = page.locator(".complete-header")
    expect(complete_header).to_have_text("Thank you for your order!")
    print("\n[PASS] Test 3: ORDER COMPLTED")
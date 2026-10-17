# pages/inventory_page.py
from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def sort_products_high_to_low(self):
        self.sort_dropdown.select_option("hilo")

    def add_first_product_to_cart(self):
        first_item_btn = self.page.locator(".inventory_item").first.locator("button")
        first_item_btn.click()

    def verify_cart_count(self, count: str):
        expect(self.cart_badge).to_have_text(count)
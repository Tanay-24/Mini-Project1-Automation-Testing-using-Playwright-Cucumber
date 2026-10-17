# mini_project1/conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        yield browser
        browser.close()

@pytest.fixture
def page(browser_instance):
    context = browser_instance.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()

# -----------------------------------------------------------
# 🌟 LINKEDIN-READY HTML REPORT CUSTOMIZATION HOOKS 🌟
# -----------------------------------------------------------

def pytest_html_report_title(report):
    report.title = "SauceDemo E2E Automation Test Report | Playwright Python"

def pytest_configure(config):
    # रिपोर्टच्या 'Environment' टेबलमध्ये कस्टम माहिती जोडणे
    if hasattr(config, "_metadata"):
        config._metadata["Project Name"] = "SauceDemo E-Commerce Automation"
        config._metadata["Automation Tool"] = "Playwright (Python Sync API)"
        config._metadata["Test Framework"] = "Pytest + Page Object Model (POM)"
        config._metadata["Quality Assurance Engineer"] = "Tanay"
        config._metadata["Execution Environment"] = "Staging / Chromium"
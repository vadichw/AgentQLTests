import time
import agentql
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright, playwright.chromium.launch(headless=False) as browser:
    page = agentql.wrap(browser.new_page(viewport={"width": 1536, "height": 800}))
    page.goto("https://www.saucedemo.com/")

    QUERY = """
    {
        username_field
        password_field
        login_btn
    }
    """

    response = page.query_elements(QUERY)

    response.username_field.type("standard_user")
    response.password_field.type("secret_sauce")
    response.login_btn.click()
    print(response)
    time.sleep(5)
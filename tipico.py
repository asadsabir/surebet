from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=100)
    context = browser.new_context()
    page = context.new_page()
    context.set_default_navigation_timeout(0)
    page.goto("https://sportsbook-co.tipico.us/home")
    page.get_by_test_id("headerLogInButton").click()
    page.get_by_test_id("login_field_email").click()
    page.get_by_test_id("login_field_email").fill("asadsabir101@gmail.com")
    page.get_by_test_id("password_field").click()
    page.get_by_test_id("password_field").fill("Mariam5200.")
    page.get_by_test_id("submit_button").click()
    page.get_by_role("listitem").filter(has_text="English Premier League").click()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


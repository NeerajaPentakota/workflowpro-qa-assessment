from playwright.sync_api import expect

def test_user_login(page):

    page.goto("https://app.workflowpro.com/login")

    page.fill("#email", "admin@company1.com")
    page.fill("#password", "password123")

    page.click("#login-btn")

    page.wait_for_url("**/dashboard")

    expect(
        page.locator(".welcome-message")
    ).to_be_visible()
def test_multi_tenant_access(page):

    page.goto("https://app.workflowpro.com/login")

    page.fill("#email", "user@company2.com")
    page.fill("#password", "password123")

    page.click("#login-btn")

    page.wait_for_load_state("networkidle")

    projects = page.locator(".project-card")

    count = projects.count()

    for i in range(count):
        assert "Company2" in projects.nth(i).text_content()
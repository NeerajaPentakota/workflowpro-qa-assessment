import requests

def test_project_creation_flow(page):

    response = requests.post(
        "https://app.workflowpro.com/api/v1/projects",
        headers={
            "Authorization":"Bearer token",
            "X-Tenant-ID":"company1"
        },
        json={
            "name":"Test Project"
        }
    )

    assert response.status_code == 201

    page.goto(
        "https://app.workflowpro.com/projects"
    )

    page.wait_for_load_state("networkidle")

    assert page.locator(
        "text=Test Project"
    ).is_visible()
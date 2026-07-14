WorkflowPro QA Assessment

Part 1 - Debugging Flaky Tests

Flakiness Issues Identified
No explicit wait after login button click.
Dashboard loads dynamically.
URL validation is too strict.
No handling for 2FA authentication.
Project cards may load slowly.
Different browsers behave differently.
Hardcoded credentials.
No screenshots or logs for debugging.
No retry mechanism.
Network latency issues in CI/CD.


Why CI/CD Fails More Frequently

CI environments are slower than local machines.
Network delays affect page loading.
Tests may run in parallel.
Different browsers render pages differently.
Dynamic elements may not load immediately.



Recommended Fixes

Use Playwright explicit waits.
Wait for URL navigation.
Wait for dashboard elements.
Add logging and screenshots.
Handle 2FA scenarios.
Use stable selectors.
Store credentials in configuration files.


# Part 2 - Test Framework Design

## Proposed Framework Structure

project
│
├── tests
│   ├── ui
│   ├── api
│   └── integration
│
├── pages
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── project_page.py
│
├── utils
│   ├── config.py
│   ├── logger.py
│   └── browserstack.py
│
├── config
│   ├── qa.yaml
│   ├── staging.yaml
│   └── production.yaml
│
├── reports
│
└── screenshots

## Framework Design Approach

### Page Object Model (POM)

Page Object Model improves:

- Reusability
- Maintainability
- Readability

Example:

```python
class LoginPage:

    def login(self,email,password):

        self.page.fill("#email",email)
        self.page.fill("#password",password)
        self.page.click("#login-btn")
```

### API Layer

Separate API utilities will handle:

- Authentication
- Project Creation
- Project Updates
- Project Deletion

### Configuration Management

Different environments:

- QA
- Staging
- Production

Example:

```yaml
base_url: https://qa.workflowpro.com
browser: chrome
tenant: company1
```

### BrowserStack Integration

BrowserStack will be used for:

- Chrome
- Firefox
- Safari
- Android Devices
- iOS Devices

### Reporting

Recommended:

- Allure Reports
- Screenshots on Failure
- Execution Logs

## Missing Requirements / Clarification Questions

1. Is 2FA mandatory for all users?
2. What reporting tool is preferred?
3. How many BrowserStack licenses are available?
4. Is parallel execution required?
5. Are mobile devices real devices or emulators?
6. What browsers and versions must be supported?
7. How should test data be cleaned up after execution?
8. What is the expected execution time for regression suites?


# Part 3 - API + UI Integration Test

## Business Scenario

Validate the complete project creation workflow across API, Web UI, Mobile Platform, and Tenant Security.

### Test Flow

Step 1:
Create Project using API

↓

Step 2:
Verify Project appears in Web UI

↓

Step 3:
Verify Project is accessible on Mobile Device

↓

Step 4:
Verify Project is only visible to correct Tenant

↓

Step 5:
Clean up Test Data

---

## Integration Test Strategy

### API Layer

Create project through API:

POST /api/v1/projects

Headers:

Authorization: Bearer Token

X-Tenant-ID: company1

Request Body:

{
"name":"Test Project",
"description":"Automation Assessment Project"
}

Expected Result:

Status Code = 201

Project created successfully.

---

### Web UI Validation

Login to company1 account.

Navigate to Projects Page.

Search for:

Test Project

Expected Result:

Project should be visible.

Project details should match API response.

---

### Mobile Validation

Open application on BrowserStack mobile device.

Login as company1 user.

Navigate to Projects screen.

Expected Result:

Project should be visible.

Project should display correctly on mobile layout.

---

### Tenant Isolation Validation

Login using company2 user.

Navigate to Projects.

Search for:

Test Project

Expected Result:

Project should NOT be visible.

This validates tenant isolation and data security.

---

## Edge Cases

### Slow API Response

Wait and retry API request.

### Slow UI Loading

Use Playwright explicit waits.

### Network Failure

Retry request and capture logs.

### Mobile Responsiveness

Validate layout on Android and iOS devices.

### Authentication Failure

Verify proper error message is displayed.

---

## Sample Test Structure

```python
def test_project_creation_flow():

    # Step 1
    # Create project via API

    # Step 2
    # Verify project in Web UI

    # Step 3
    # Verify project on Mobile

    # Step 4
    # Verify Tenant Isolation

    pass
```

## Test Data Management

Use unique project names:

TestProject_20260714_001

Benefits:

- Avoid duplicate data
- Support parallel execution
- Easier cleanup

## Cleanup Strategy

Delete created project after execution.

This keeps test environments clean and reusable.

# Assumptions

1. Authentication token is available for API testing.
2. BrowserStack account and devices are configured.
3. Test users exist for company1 and company2.
4. Test environment supports project creation and deletion.
5. Tenant isolation is enforced using X-Tenant-ID header.
6. Mobile testing is performed using BrowserStack real devices.
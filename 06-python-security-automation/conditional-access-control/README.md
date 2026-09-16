# Python Conditional Access-Control Automation

## Project Overview

This project uses Python conditional statements to automate two routine security decisions:

1. Determine whether a device's operating system requires an update.
2. Approve or deny a login based on the username and whether the attempt occurred during organization hours.

The project began as a guided notebook exercise and was refactored into a reusable Python script with functions, clear decision paths, input validation, and test scenarios.

## Scenario

As a security analyst, I needed to reduce repetitive manual checks. The first requirement was to recognize whether `OS 1`, `OS 2`, or `OS 3` required an update. The second was to evaluate login attempts to a specific device against an approved-user list and an organization-hours rule.

## Security Rules

### Operating-system status

| System | Decision |
|---|---|
| `OS 1` | Update required |
| `OS 2` | No update required |
| `OS 3` | Update required |
| Any other value | Manual review required |

### Login authorization

A login is granted only when both conditions are true:

- The username appears in the approved-user set.
- The attempt occurs during organization hours.

This is represented by:

```python
if username in APPROVED_USERS and organization_hours:
    return "Login attempt approved during organization hours."
```

## Decision Matrix

| Approved User | Organization Hours | Result |
|---|---|---|
| Yes | Yes | Grant access |
| Yes | No | Deny access |
| No | Yes | Deny access |
| No | No | Deny access |

## Corrected Logic

During review, I corrected several common conditional-statement errors from the working notebook.

### Comparing multiple usernames

This expression is unsafe:

```python
if username == approved_user1 or approved_user2:
```

Python evaluates a non-empty string such as `approved_user2` as truthy, so the condition can approve an unauthorized username. Each comparison must be explicit:

```python
if username == approved_user1 or username == approved_user2:
```

For a larger group, membership testing is cleaner:

```python
if username in APPROVED_USERS:
```

### Combining operating-system conditions

This expression does not test the variable against both values:

```python
elif "OS 1" or "OS 3":
```

The string `"OS 1"` is always truthy. The corrected form is:

```python
elif system == "OS 1" or system == "OS 3":
```

The final script uses set membership for clarity:

```python
if system in OUTDATED_SYSTEMS:
    return "Update needed."
```

## Implementation

The complete program is available in [`access_control.py`](access_control.py).

### System update function

```python
def check_system_update(system: str) -> str:
    if system == CURRENT_OS:
        return "No update needed."
    if system in OUTDATED_SYSTEMS:
        return "Update needed."
    return "Unknown operating system. Manual review required."
```

The final branch fails safely by sending unrecognized values to manual review instead of assuming that an unknown system is approved or automatically applying the wrong response.

### Login decision function

```python
def check_device_access(username: str, organization_hours: bool) -> str:
    if username in APPROVED_USERS and organization_hours:
        return "Login attempt approved during organization hours."
    return "Login denied: username not approved or outside organization hours."
```

## Test Scenarios

The script evaluates all four combinations of authorization and time:

```python
login_attempts = [
    ("bmoreno", True),
    ("bmoreno", False),
    ("unknown_user", True),
    ("unknown_user", False),
]
```

Expected results:

- `bmoreno` during organization hours: approved.
- `bmoreno` outside organization hours: denied.
- `unknown_user` during organization hours: denied.
- `unknown_user` outside organization hours: denied.

## Security Analysis

This script demonstrates the logic behind an access decision, but production authorization requires additional safeguards:

- Strong authentication and multi-factor authentication
- Trusted identity and role data
- Server-controlled time and timezone handling
- Logging of every decision and login attempt
- Rate limiting and account-lockout safeguards
- Secure failure when information is missing or malformed
- Centralized policy enforcement instead of relying on client-side code
- Regular review of the approved-user list

An organization should not use time of day as its only authorization control. A valid user working outside normal hours might require additional verification rather than automatic permanent denial, depending on business policy.

## Key Takeaways

- `if`, `elif`, and `else` create controlled decision paths.
- `in` is an effective membership test for allow lists.
- `and` requires both security conditions to be true.
- Non-empty strings are truthy and can cause accidental authorization when conditions are written incorrectly.
- Unknown inputs should produce a safe, explicit result.
- Testing every branch is essential for security-sensitive logic.
- Reusable functions are easier to test and maintain than repeated code cells.

## Skills Demonstrated

- Python conditional statements
- Boolean and logical operators
- Allow-list membership checks
- Secure access-decision logic
- Function design and code refactoring
- Test-case development
- Input handling and fail-safe decisions
- Security automation documentation

## How to Run

```bash
python3 access_control.py
```

## Project Note

This portfolio project is based on a guided cybersecurity training activity. The final script was corrected and refactored as an original security-automation example.

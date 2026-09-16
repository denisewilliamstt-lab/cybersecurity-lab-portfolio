"""Security automation examples using Python conditional statements."""


APPROVED_USERS = {"elarson", "bmoreno", "tshah", "sgilmore", "eraab"}
CURRENT_OS = "OS 2"
OUTDATED_SYSTEMS = {"OS 1", "OS 3"}


def check_system_update(system: str) -> str:
    """Return the update status for a recognized operating system."""
    if system == CURRENT_OS:
        return "No update needed."
    if system in OUTDATED_SYSTEMS:
        return "Update needed."
    return "Unknown operating system. Manual review required."


def check_device_access(username: str, organization_hours: bool) -> str:
    """Approve login only for an allowed user during organization hours."""
    if username in APPROVED_USERS and organization_hours:
        return "Login attempt approved during organization hours."
    return "Login denied: username not approved or outside organization hours."


def evaluate_login(username: str, organization_hours: bool) -> dict[str, object]:
    """Return structured evidence about a login decision."""
    approved_user = username in APPROVED_USERS
    access_granted = approved_user and organization_hours

    return {
        "username": username,
        "approved_user": approved_user,
        "organization_hours": organization_hours,
        "access_granted": access_granted,
        "message": check_device_access(username, organization_hours),
    }


if __name__ == "__main__":
    systems = ["OS 1", "OS 2", "OS 3", "OS 4"]
    login_attempts = [
        ("bmoreno", True),
        ("bmoreno", False),
        ("unknown_user", True),
        ("unknown_user", False),
    ]

    print("Operating-system update checks")
    for operating_system in systems:
        print(f"{operating_system}: {check_system_update(operating_system)}")

    print("\nLogin access checks")
    for user, during_hours in login_attempts:
        result = evaluate_login(user, during_hours)
        print(result)

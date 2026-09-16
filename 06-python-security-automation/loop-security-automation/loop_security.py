"""Security automation examples using Python for and while loops."""


ALLOW_LIST = {
    "192.168.243.140",
    "192.168.205.12",
    "192.168.151.162",
    "192.168.178.71",
    "192.168.86.232",
    "192.168.3.24",
    "192.168.170.243",
    "192.168.119.173",
}

LOGIN_ATTEMPTS = [
    "192.168.142.245",
    "192.168.109.50",
    "192.168.86.232",
    "192.168.131.147",
    "192.168.205.12",
    "192.168.200.48",
]


def connection_failure_messages(connection_attempts: int) -> list[str]:
    """Create one failure message for every unsuccessful connection attempt."""
    if connection_attempts < 0:
        raise ValueError("connection_attempts cannot be negative")

    messages = []
    for _ in range(connection_attempts):
        messages.append("Connection could not be established.")
    return messages


def evaluate_ip_attempts(
    ip_addresses: list[str],
    allow_list: set[str],
    stop_on_denied: bool = False,
) -> list[dict[str, object]]:
    """Evaluate attempted source IPs and optionally stop at the first denial."""
    results = []

    for ip_address in ip_addresses:
        allowed = ip_address in allow_list
        result = {
            "ip_address": ip_address,
            "allowed": allowed,
            "message": "IP address is allowed."
            if allowed
            else "IP address is not allowed. Further investigation required.",
        }
        results.append(result)

        if not allowed and stop_on_denied:
            break

    return results


def generate_sales_ids(start: int = 5000, end: int = 5150) -> list[int]:
    """Generate unique Sales IDs divisible by five within an inclusive range."""
    if start > end:
        raise ValueError("start must not be greater than end")

    employee_ids = []
    current_id = start

    remainder = current_id % 5
    if remainder:
        current_id += 5 - remainder

    while current_id <= end:
        employee_ids.append(current_id)
        current_id += 5

    return employee_ids


if __name__ == "__main__":
    print("Connection attempt messages")
    for message in connection_failure_messages(3):
        print(message)

    print("\nAll IP address decisions")
    for decision in evaluate_ip_attempts(LOGIN_ATTEMPTS, ALLOW_LIST):
        print(decision)

    print("\nRestricted-data investigation mode")
    for decision in evaluate_ip_attempts(
        LOGIN_ATTEMPTS, ALLOW_LIST, stop_on_denied=True
    ):
        print(decision)

    print("\nSales employee IDs")
    for employee_id in generate_sales_ids():
        print(employee_id)
        if employee_id == 5100:
            print("Only 10 valid employee IDs remaining.")

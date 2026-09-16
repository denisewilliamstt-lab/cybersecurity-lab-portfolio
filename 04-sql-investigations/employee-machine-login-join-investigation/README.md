# SQL JOIN Investigation: Employees, Machines, and Login Activity

## Project Overview

This project uses SQL joins to support an investigation into compromised company machines. Information stored across the `machines`, `employees`, and `log_in_attempts` tables was combined to identify device assignments, expose unassigned assets and employees, and connect users with their authentication activity.

## Investigation Objectives

- Match employees to their assigned machines.
- Identify machines that are not assigned to an employee.
- Identify employees who do not have a machine assigned.
- Retrieve employee information alongside recorded login attempts.

## Data Relationships

| Table | Relevant field | Investigation use |
|---|---|---|
| `machines` | `device_id` | Identifies each company machine |
| `employees` | `device_id`, `username` | Connects employees to devices and login activity |
| `log_in_attempts` | `username` | Records authentication attempts by user |

The `device_id` field connects machines with employees. The `username` field connects employees with login attempts.

## Investigation

### 1. Match employees to assigned machines

An `INNER JOIN` returns only records with matching device IDs in both tables.

```sql
SELECT
    m.device_id,
    e.username,
    m.operating_system
FROM machines AS m
INNER JOIN employees AS e
    ON m.device_id = e.device_id;
```

**Result:** 185 matching records were returned.

**Interpretation:** These records connect known employees with assigned company machines. Unmatched machines and employees are excluded.

### 2. Preserve all machines

A `LEFT JOIN` keeps every machine, including devices without a matching employee.

```sql
SELECT
    m.device_id,
    m.operating_system,
    e.username
FROM machines AS m
LEFT JOIN employees AS e
    ON m.device_id = e.device_id;
```

**Result:** The final returned record contained `NULL` in the `username` field.

**Interpretation:** A `NULL` employee value indicates an unassigned machine. These devices should be reviewed to confirm their owner, status, location, and authorization.

### 3. Preserve all employees

The lab used a `RIGHT JOIN` to keep every employee, even when no machine matched.

```sql
SELECT
    m.device_id,
    m.operating_system,
    e.username
FROM machines AS m
RIGHT JOIN employees AS e
    ON m.device_id = e.device_id;
```

**Result:** The final username returned was `areyes`.

The same logic can usually be written more readably by reversing the table order and using a `LEFT JOIN`:

```sql
SELECT
    m.device_id,
    m.operating_system,
    e.username
FROM employees AS e
LEFT JOIN machines AS m
    ON e.device_id = m.device_id;
```

**Interpretation:** Employees with `NULL` machine fields have no assigned device and may require provisioning or an access review.

### 4. Connect employees to login attempts

An `INNER JOIN` on `username` associates employee records with authentication activity.

```sql
SELECT
    e.username,
    l.*
FROM employees AS e
INNER JOIN log_in_attempts AS l
    ON e.username = l.username;
```

**Result:** 200 login-attempt records were returned.

**Interpretation:** The joined data gives investigators employee context for each matching login attempt. It can be filtered further to examine failed attempts, unusual locations, off-hours activity, or accounts associated with compromised machines.

## Supplemental Audit Queries

These focused queries isolate gaps instead of requiring an analyst to scan a complete result set.

### Find unassigned machines

```sql
SELECT m.*
FROM machines AS m
LEFT JOIN employees AS e
    ON m.device_id = e.device_id
WHERE e.device_id IS NULL;
```

### Find employees without assigned machines

```sql
SELECT e.*
FROM employees AS e
LEFT JOIN machines AS m
    ON e.device_id = m.device_id
WHERE m.device_id IS NULL;
```

## Security Findings

- SQL joins can correlate asset, identity, and authentication data during an investigation.
- Unassigned machines may represent inventory, configuration, or access-control gaps.
- Employees without assigned devices may require provisioning validation.
- Authentication records become more useful when joined with employee identity data.
- Selecting specific columns produces clearer evidence than using `SELECT *` in a final report.

## Skills Demonstrated

- Relational database analysis
- `INNER JOIN`, `LEFT JOIN`, and `RIGHT JOIN`
- Table aliases and qualified column names
- Identification of unmatched records with `NULL`
- Asset-to-user correlation
- Authentication-log investigation
- Security-focused interpretation of query results

## Files

- [queries.sql](queries.sql) — documented SQL used in the investigation

## Key Takeaway

SQL joins allow a security analyst to combine otherwise isolated records into useful investigative evidence. Choosing the correct join type determines whether the analysis includes only confirmed matches or also exposes missing relationships that may indicate security and asset-management gaps.

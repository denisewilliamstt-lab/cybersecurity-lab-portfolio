-- SQL JOIN Investigation
-- Tables: machines, employees, log_in_attempts

-- 1. Match employees to assigned machines.
SELECT
    m.device_id,
    e.username,
    m.operating_system
FROM machines AS m
INNER JOIN employees AS e
    ON m.device_id = e.device_id;

-- 2. Preserve all machines, including unassigned devices.
SELECT
    m.device_id,
    m.operating_system,
    e.username
FROM machines AS m
LEFT JOIN employees AS e
    ON m.device_id = e.device_id;

-- 3. Preserve all employees using the RIGHT JOIN demonstrated in the lab.
SELECT
    m.device_id,
    m.operating_system,
    e.username
FROM machines AS m
RIGHT JOIN employees AS e
    ON m.device_id = e.device_id;

-- 4. Equivalent employee-first query using LEFT JOIN.
SELECT
    m.device_id,
    m.operating_system,
    e.username
FROM employees AS e
LEFT JOIN machines AS m
    ON e.device_id = m.device_id;

-- 5. Connect employees to recorded login attempts.
SELECT
    e.username,
    l.*
FROM employees AS e
INNER JOIN log_in_attempts AS l
    ON e.username = l.username;

-- 6. Isolate machines that have no assigned employee.
SELECT m.*
FROM machines AS m
LEFT JOIN employees AS e
    ON m.device_id = e.device_id
WHERE e.device_id IS NULL;

-- 7. Isolate employees who have no assigned machine.
SELECT e.*
FROM employees AS e
LEFT JOIN machines AS m
    ON e.device_id = m.device_id
WHERE m.device_id IS NULL;

1. SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id;

2.SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id;


3.SELECT e.first_name, e.last_name, e.department_id, d.department_name
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id
WHERE e.department_id IN (40, 80);


4.SELECT d.department_id, d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments AS d
LEFT JOIN employees AS e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name;


5.SELECT e.first_name AS employee_name, m.first_name AS manager_name
FROM employees AS e
LEFT JOIN employees AS m ON e.manager_id = m.employee_id;


6.SELECT e.first_name || ' ' || e.last_name AS full_name, e.job_title,
       (j.max_salary - e.salary) AS salary_difference
FROM employees AS e
JOIN jobs AS j ON e.job_id = j.job_id;


7.SELECT j.job_title, AVG(e.salary) AS average_salary
FROM employees AS e
JOIN jobs AS j ON e.job_id = j.job_id
GROUP BY j.job_title;


8.SELECT e.first_name || ' ' || e.last_name AS full_name, e.salary
FROM employees AS e
JOIN departments AS d ON e.department_id = d.department_id
JOIN locations AS l ON d.location_id =



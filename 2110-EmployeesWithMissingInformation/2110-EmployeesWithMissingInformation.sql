-- Last updated: 4/20/2026, 1:25:22 PM
# Write your MySQL query statement below
select employee_id from
(SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
UNION 
SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id)) a
WHERE salary is null
order by employee_id
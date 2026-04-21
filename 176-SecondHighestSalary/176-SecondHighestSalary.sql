-- Last updated: 4/21/2026, 8:41:54 AM
# Write your MySQL query statement below
select max(salary) as SecondHighestSalary from employee
where salary<(select max(salary) from employee)
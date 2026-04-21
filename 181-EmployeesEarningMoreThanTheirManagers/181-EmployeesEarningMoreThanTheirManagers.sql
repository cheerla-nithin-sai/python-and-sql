-- Last updated: 4/21/2026, 8:41:46 AM
# Write your MySQL query statement below
select e.name as `employee` from employee e
inner join employee d on d.id=e.managerId and e.salary>d.salary
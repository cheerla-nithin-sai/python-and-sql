-- Last updated: 4/21/2026, 8:41:42 AM
# Write your MySQL query statement below
with cte as (select d.name as Department,e.name as Employee ,salary,rank()over(partition by departmentId order by salary desc) as rn
from Employee e
left join Department d on d.id=e.departmentId)
select Department,Employee,salary from cte
where rn=1
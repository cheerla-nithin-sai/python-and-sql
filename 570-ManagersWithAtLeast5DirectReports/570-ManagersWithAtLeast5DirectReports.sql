-- Last updated: 4/21/2026, 8:40:53 AM
-- Write your PostgreSQL query statement below
select a.name from employee a
left join employee b on a.id=b.managerId
group by a.id,a.name
having count(b.managerId)>=5


-- Last updated: 4/20/2026, 1:25:29 PM
# Write your MySQL query statement below
with cats as (select 'Low Salary' as category
union all select 'Average Salary'
union all select 'High Salary'),
rnk as(
select *,
case when income<20000 then 'Low Salary' 
when income between 20000 and 50000 then 'Average Salary'
when income>50000 then 'High Salary' end as category
from Accounts)
select c.category,count(account_id) as accounts_count from cats c
left join rnk r on c.category=r.category
group by r.category

-- Last updated: 4/20/2026, 1:26:07 PM
# Write your MySQL query statement below
select contest_id,round(100*((count(distinct user_id))/(select count(user_id) from users)),2) as percentage
from register 
group by contest_id
order by percentage desc,contest_id
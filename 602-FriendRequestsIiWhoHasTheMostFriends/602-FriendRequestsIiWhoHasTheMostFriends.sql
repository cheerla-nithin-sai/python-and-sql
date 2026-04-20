-- Last updated: 4/20/2026, 1:28:27 PM
# Write your MySQL query statement below
with cte as (select requester_id from RequestAccepted
union all
select accepter_id from RequestAccepted)
select requester_id as id ,count(*) as num
from cte
group by requester_id
order by num desc
limit 1

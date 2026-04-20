-- Last updated: 4/20/2026, 1:25:27 PM
# Write your MySQL query statement below
select a.user_id,
ifnull(round(sum(case when action="confirmed" then 1 else 0 end)/(sum(case when action="timeout" then 1 else 0 end)+sum(case when action="confirmed" then 1 else 0 end)),2),0) as confirmation_rate
from signups a
left join confirmations c on a.user_id=c.user_id
group by a.user_id
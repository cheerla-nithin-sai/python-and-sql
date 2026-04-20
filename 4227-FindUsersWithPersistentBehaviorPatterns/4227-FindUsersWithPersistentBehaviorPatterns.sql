-- Last updated: 4/20/2026, 1:23:46 PM
# Write your MySQL query statement below
with cte as (select user_id,action,count(distinct(action_date)) as streak_length, min(action_date) as start_date,max(action_date) as end_date
from activity a
group by user_id,action
having streak_length>=5 and max(action_date)-min(action_date)>=4
order by streak_length desc)
select * from cte
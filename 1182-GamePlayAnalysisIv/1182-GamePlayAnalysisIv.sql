-- Last updated: 4/20/2026, 1:27:32 PM
# Write your MySQL query statement below
-- with cte as (select player_id,min(event_date) as first_login from activity)
-- select round(count(distinct cte.player_id)/count(distinct activity.player_id),2) as fraction 
-- from activity
-- left join cte on cte.player_id=activity.player_id and first_login = DATE_SUB(event_date, INTERVAL 1 DAY)

-- count(distinct(case when datediff(day,event_date,first_login)=1 then activity.player_id end)),count(distinct activity.player_id) from activity

select round(sum(ln)/count(distinct player_id),2) as fraction from (
select player_id,datediff(event_date,min(event_date)over(partition by player_id))=1 as ln
from activity) a
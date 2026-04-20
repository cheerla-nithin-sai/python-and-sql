-- Last updated: 4/20/2026, 1:23:57 PM
# Write your MySQL query statement below
select session_id,user_id,timestampdiff(minute,min(event_timestamp),max(event_timestamp)) as session_duration_minutes,
sum(case when event_type='scroll' then 1 else 0 end) as scroll_count
from app_events
group by session_id,user_id
having (sum(case when event_type='click' then 1 else 0 end)*1.0/sum(case when event_type='scroll' then 1 else 0 end)<0.2) and scroll_count>=5 and session_duration_minutes>30 and sum(case when event_type='purchase' then 1 else 0 end)=0
order by scroll_count desc,session_id;

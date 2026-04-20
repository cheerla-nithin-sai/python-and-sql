-- Last updated: 4/20/2026, 1:23:55 PM
# Write your MySQL query statement below
with last_event as(select user_id,event_type,row_number()over(partition by user_id order by event_date desc) as rn,plan_name as current_plan,monthly_amount as current_monthly_amount
from subscription_events
order by user_id,event_date desc),
cte as (select user_id,sum(case when event_type='downgrade' then 1 else 0
end) as down_cust,datediff(max(event_date),min(event_date)) as dt_diff,
max(monthly_amount) as max_historical_amount
 from subscription_events
group by user_id
having down_cust>=1 and dt_diff>=60)
select cte.user_id,current_plan,current_monthly_amount,max_historical_amount,dt_diff as days_as_subscriber
from cte
join last_event on last_event.user_id=cte.user_id and rn=1 and event_type!='cancel' and current_monthly_amount/max_historical_amount<0.5
order by days_as_subscriber desc, user_id
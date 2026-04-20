-- Last updated: 4/20/2026, 1:24:18 PM
# Write your MySQL query statement bel
with free_tr as (
    select user_id,round(avg(activity_duration),2) as trial_avg_duration
    from UserActivity u
    where activity_type='free_trial'
    group by user_id
),
paid_tr as (
    select user_id,round(avg(activity_duration),2) as paid_avg_duration
    from UserActivity u
    where activity_type='paid'
    group by user_id
)
select f.user_id,trial_avg_duration,paid_avg_duration from free_tr f
inner join paid_tr p on p.user_id=f.user_id
order by f.user_id
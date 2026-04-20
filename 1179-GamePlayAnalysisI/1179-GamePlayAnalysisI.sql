-- Last updated: 4/20/2026, 1:27:36 PM
# Write your MySQL query statement below
select player_id,min(event_date) as first_login
from activity
group by player_id
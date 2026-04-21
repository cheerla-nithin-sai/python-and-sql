-- Last updated: 4/21/2026, 8:41:48 AM
# Write your MySQL query statement below
select score,dense_rank()over(order by score desc) as `rank`
from Scores
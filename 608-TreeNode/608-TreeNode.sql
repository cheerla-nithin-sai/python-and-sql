-- Last updated: 4/20/2026, 1:28:25 PM
# Write your MySQL query statement below
select id,case when p_id is null then 'Root'
               when id in (select p_id from Tree)then 'Inner'
               else 'Leaf' end as type
from Tree
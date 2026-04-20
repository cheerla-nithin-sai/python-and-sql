-- Last updated: 4/20/2026, 1:28:23 PM
# Write your MySQL query statement below
select *,case when x+y>z and y+z>x and x+z>y then 'Yes' else 'No' end as triangle
from Triangle
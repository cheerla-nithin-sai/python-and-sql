-- Last updated: 4/20/2026, 1:28:21 PM
with cte as(select count(*) as ct from seat)
select case when id=ct and id%2!=0 then id when id%2!=0 then id+1 else id-1 end as id,student
from Seat
cross join cte
order by id
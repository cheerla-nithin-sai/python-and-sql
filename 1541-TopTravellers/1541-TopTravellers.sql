-- Last updated: 4/20/2026, 1:26:23 PM
# Write your MySQL query statement below
select u.name,ifnull(sum(distance),0) as travelled_distance 
from users u left join rides r on r.user_id=u.id 
group by u.id order by travelled_distance desc,name
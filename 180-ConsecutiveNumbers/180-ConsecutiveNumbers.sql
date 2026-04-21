-- Last updated: 4/21/2026, 8:41:47 AM
# Write your MySQL query statement below
select distinct l1.num ConsecutiveNums
from logs l1, logs l2, logs l3
where  
l1.Id = l2.Id - 1
AND l2.Id = l3.Id - 1
AND l1.Num = l2.Num
AND l2.Num = l3.Num
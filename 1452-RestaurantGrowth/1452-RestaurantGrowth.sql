-- Last updated: 4/20/2026, 1:27:07 PM
# Write your MySQL query statement below
with art as (select visited_on,sum(amount) as amount
from customer
group by visited_on),
cte as (select visited_on,sum(amount) over(order by visited_on rows between 6 preceding and current row) as amount,
round(avg(amount)over(order by visited_on rows between 6 preceding and current row),2) as average_amount,
row_number()over(order by visited_on) as rn
from art)
select visited_on,amount,average_amount
from cte
where rn>6
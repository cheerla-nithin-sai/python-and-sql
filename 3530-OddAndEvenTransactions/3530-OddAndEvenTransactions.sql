-- Last updated: 4/20/2026, 1:24:25 PM
# Write your MySQL query statement below
with cte as (select *,case when amount%2=0 then amount else 0 end as even_amt,case when amount%2!=0 then amount else 0 end as odd_amt
from transactions)
select transaction_date,sum(odd_amt) as odd_sum,sum(even_amt) as even_sum
from cte
group by transaction_date
order by transaction_date
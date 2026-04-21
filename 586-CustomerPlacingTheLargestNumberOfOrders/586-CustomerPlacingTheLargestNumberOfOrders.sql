-- Last updated: 4/21/2026, 8:40:50 AM

select customer_number
from (select customer_number,count(order_number) as ct 
from orders
group by customer_number
order by count(order_number) desc
limit 1) as s

-- Last updated: 4/20/2026, 1:26:36 PM
# Write your MySQL query statement below
select product_name,sum(unit) as unit
from products p
left join orders o on o.product_id=p.product_id
where  year(order_date)=2020 and month(order_date)=02
group by product_name
having unit>99
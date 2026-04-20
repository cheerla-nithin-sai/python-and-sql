-- Last updated: 4/20/2026, 1:23:56 PM
# Write your MySQL query statement below
select customer_id,count(order_id) as total_orders,round(sum(case when hour(order_timestamp) in (11,12,13,18,19,20) then 1 else 0 end)/count(order_id)*100,0) as peak_hour_percentage,round(avg(order_rating),2) as average_rating
from restaurant_orders
group by customer_id
having peak_hour_percentage>=60 and average_rating>=4 and count(case when order_rating is not null then order_id end)/count(order_id)>=0.5 and total_orders>=3
order by average_rating desc,customer_id desc

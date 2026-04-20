-- Last updated: 4/20/2026, 1:27:16 PM
-- Write your PostgreSQL query statement below
select p.product_id,coalesce(round(sum(p.price*u.units)::decimal/sum(u.units),2),0)as average_price from prices p
left join unitssold u on u.product_id=p.product_id and (u.purchase_date between p.start_date and p.end_date)
group by p.product_id
-- Last updated: 4/20/2026, 1:27:37 PM
# Write your MySQL query statement below
with cte as (select product_id,min(year) as first_year from sales group by product_id)
select cte.*,quantity,price from cte
left join sales on sales.product_id=cte.product_id and first_year=sales.year

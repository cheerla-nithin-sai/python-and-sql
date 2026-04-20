-- Last updated: 4/20/2026, 1:24:12 PM
# Write your MySQL query statement below
with cte as (select a.category as category1,p.category as category2,a.product_id as prod1,p.product_id as prod2 from productInfo a
left join productInfo p on a.category<p.category), cte2 as (select a.user_id,a.product_id as prod1,b.product_id as prod2 from ProductPurchases a
left join ProductPurchases b on a.user_id=b.user_id)
select category1,category2,count(distinct user_id) as customer_count from cte
inner join cte2 on cte2.prod1=cte.prod1 and cte2.prod2=cte.prod2
group by category1,category2
having count(distinct user_id)>=3
order by 3 desc,category1,category2
-- select cat1,cat2,count(distinct user_id) as ct from cte c
-- inner join ProductPurchases p on p.product_id=c.prod1 or p.product_id=c.prod2
-- group by cat1,cat2
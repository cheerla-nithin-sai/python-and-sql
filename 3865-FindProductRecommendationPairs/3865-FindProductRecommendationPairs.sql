-- Last updated: 4/20/2026, 1:24:16 PM
# Write your MySQL query statement below
select p.product_id as product1_id,q.product_id as product2_id,r.category as product1_category,s.category as product2_category,count(distinct p.user_id)  as customer_count
from ProductPurchases p 
inner join productpurchases q on q.user_id=p.user_id and p.product_id<q.product_id
left join productInfo r on r.product_id=p.product_id
left join productInfo s on s.product_id=q.product_id
group by product1_id,product2_id
having customer_count>=3
order by customer_count desc,product1_id,product2_id
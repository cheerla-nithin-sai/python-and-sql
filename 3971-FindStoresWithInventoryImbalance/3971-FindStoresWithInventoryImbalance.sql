-- Last updated: 4/20/2026, 1:24:03 PM
# Write your MySQL query statement below
with high_prds as (
    select store_id,product_name as most_exp_product,price as high_price,quantity as high_quantity,row_number()over(partition by store_id order by price desc) as rn_high
    from inventory
),
low_prods as (select store_id,product_name as cheapest_product,price as low_price,quantity as low_quantity,
row_number()over(partition by store_id order by price) as rn_low
    from inventory)
select h.store_id,store_name,location,most_exp_product,cheapest_product,round(low_quantity/high_quantity,2) as imbalance_ratio
from high_prds h
inner join low_prods l on l.store_id=h.store_id and rn_high=1 and rn_low=1 and high_quantity<low_quantity
inner join stores s on s.store_id=h.store_id
where h.store_id in (select store_id from inventory
group by store_id
having count(distinct(product_name))>=3)
order by imbalance_ratio desc,store_name

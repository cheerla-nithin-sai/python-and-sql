-- Last updated: 4/20/2026, 1:28:26 PM
# Write your MySQL query statement below
select name from salesperson 
where sales_id not in (select sales_id from orders o left join Company c on c.com_id=o.com_id
where c.name='RED');
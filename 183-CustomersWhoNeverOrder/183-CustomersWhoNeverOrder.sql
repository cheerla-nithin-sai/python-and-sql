-- Last updated: 4/21/2026, 8:41:44 AM
# Write your MySQL query statement below
select name as Customers from Customers
where id not in (select customerId from orders)
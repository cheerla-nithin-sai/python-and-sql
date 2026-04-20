-- Last updated: 4/20/2026, 1:24:09 PM
# Write your MySQL query statement below

with cte as (select employee_id,rating,row_number()over(partition by employee_id order by review_date desc) as dt_rn,
lag(rating,1) over(partition by employee_id order by review_date desc) as lg,
lag(rating,2) over(partition by employee_id order by review_date desc) as sg
 from performance_reviews)
 select c.employee_id,name,sg-rating as improvement_score from cte c
 left join employees e on e.employee_id=c.employee_id
 where dt_rn=3 and rating<lg and lg<sg
 order by improvement_score desc,name
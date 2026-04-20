-- Last updated: 4/20/2026, 1:27:15 PM
# Write your MySQL query statement below
select query_name,round(avg(rating/position),2) as quality,round(100*(avg(rating<3)),2) as poor_query_percentage from queries
group by query_name
having query_name is not null
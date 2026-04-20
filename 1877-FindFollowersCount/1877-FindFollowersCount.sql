-- Last updated: 4/20/2026, 1:25:53 PM
# Write your MySQL query statement below
select user_id,count(follower_id) as followers_count from followers
group by user_id
order by user_id
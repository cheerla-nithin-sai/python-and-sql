-- Last updated: 4/20/2026, 1:23:45 PM
# Write your MySQL query statement below
with cte as (select user_id,count(*) as ct from reactions group by user_id)
select r.user_id,reaction as dominant_reaction,round(count(*)/ct,2) as reaction_ratio from reactions r
left join cte on cte.user_id=r.user_id
where r.user_id in (select user_id from reactions
group by user_id
having count(distinct content_id)>4)
group by r.user_id,reaction
having reaction_ratio>=0.6
order by reaction_ratio desc, user_id
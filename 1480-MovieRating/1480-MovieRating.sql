-- Last updated: 4/20/2026, 1:26:33 PM
# Write your MySQL query statement below
(select u.name as results from users u
right join movierating m on m.user_id=u.user_id
group by u.user_id
order by count(m.movie_id) desc,u.name
limit 1)
union all
(select m.title from movies m
right join movierating r on r.movie_id=m.movie_id
where r.created_at like "2020-02%"
group by r.movie_id 
order by avg(r.rating) desc,m.title
limit 1

)
-- Last updated: 4/20/2026, 1:24:00 PM
# Write your MySQL query statement below
select b.*,max(session_rating)-min(session_rating) as rating_spread,
round(sum(case when session_rating>=4 or session_rating<=2 then 1 else 0 end)/count(session_id),2) as polarization_score
from reading_sessions r
inner join books b on b.book_id=r.book_id
group by book_id
having count(session_id)>=5 and sum(case when session_rating>=4 then 1 end)>0 and sum(case when session_rating<=2 then 1 end)>0 and polarization_score>=0.6
order by polarization_score desc,title desc
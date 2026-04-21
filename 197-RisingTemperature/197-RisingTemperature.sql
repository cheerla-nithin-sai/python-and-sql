-- Last updated: 4/21/2026, 8:41:40 AM
# Write your MySQL query statement below
select q.id from weather q
inner join weather b on q.temperature>b.temperature and datediff(q.recordDate,b.recordDate)=1
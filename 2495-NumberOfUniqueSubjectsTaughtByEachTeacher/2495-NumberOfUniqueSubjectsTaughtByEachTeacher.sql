-- Last updated: 4/20/2026, 1:25:07 PM
# Write your MySQL query statement below
select teacher_id,count(distinct subject_id) as cnt from Teacher
group by teacher_id

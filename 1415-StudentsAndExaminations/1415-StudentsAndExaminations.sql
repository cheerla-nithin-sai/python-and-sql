-- Last updated: 4/20/2026, 1:27:11 PM
-- Write your PostgreSQL query statement below
select x.student_id,x.student_name,s.subject_name,count(e.student_id) as attended_exams from students x
cross join subjects s 
left join examinations e on e.student_id=x.student_id and e.subject_name=s.subject_name
group by x.student_id,x.student_name,s.subject_name
order by x.student_id,s.subject_name
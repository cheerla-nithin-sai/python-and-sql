-- Last updated: 4/20/2026, 1:24:08 PM
# Write your MySQL query statement below
with first_date as (select patient_id,min(test_date) as post_date
from covid_tests 
where result like 'Pos%'
group by patient_id),
 rec_date as (select patient_id,test_date as rec_date
from covid_tests 
where result like 'Neg%')
select f.patient_id,patient_name,age,datediff(min(rec_date),post_date) as recovery_time from first_date f
inner join rec_date s on s.patient_id=f.patient_id and f.post_date<s.rec_date
left join patients p on p.patient_id=f.patient_id
group by f.patient_id
order by 4,2
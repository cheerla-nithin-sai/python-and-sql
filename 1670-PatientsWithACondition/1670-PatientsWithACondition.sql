-- Last updated: 4/20/2026, 1:26:14 PM
# Write your MySQL query statement below
select * from patients
where conditions LIKE ("DIAB1%") OR conditions like ("% DIAB1%")
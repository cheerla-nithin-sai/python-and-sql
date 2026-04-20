-- Last updated: 4/20/2026, 1:28:20 PM
# Write your MySQL query statement below
update Salary
set sex=case when sex='m' then 'f' else 'm' end;
-- Last updated: 4/20/2026, 1:24:05 PM
with weekly_hours as (select m.employee_id,year(m.meeting_date) as 'year',week(m.meeting_date, 1) as 'week',sum(m.duration_hours) as 'total_hours' from meetings m group by m.employee_id, year, week)

,heavy_weeks as (select employee_id,count(*) as meeting_heavy_weeks from weekly_hours where total_hours > 20 group by employee_id ) 

select e.employee_id,e.employee_name,e.department,h.meeting_heavy_weeks from heavy_weeks h join employees e on e.employee_id = h.employee_id where h.meeting_heavy_weeks >= 2 order by h.meeting_heavy_weeks desc, e.employee_name;
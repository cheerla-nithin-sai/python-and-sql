-- Last updated: 4/20/2026, 1:24:07 PM
# Write your MySQL query statement below
with first_half as (
    select driver_id,sum(distance_km/fuel_consumed)/count(trip_id) as first_half_avg
    from trips
    where month(trip_date) in (1,2,3,4,5,6)
    group by driver_id
),
second_half as (
    select driver_id,sum(distance_km/fuel_consumed)/count(trip_id) as second_half_avg
    from trips
    where month(trip_date) in (7,8,9,10,11,12)
    group by driver_id
)
select f.driver_id,d.driver_name,round(f.first_half_avg,2) as first_half_avg,round(s.second_half_avg,2) as second_half_avg,round(second_half_avg-first_half_avg,2) as efficiency_improvement from first_half f
inner join second_half s on s.driver_id=f.driver_id and second_half_avg>first_half_avg
inner join drivers d on d.driver_id=f.driver_id
order by 5 desc,driver_name
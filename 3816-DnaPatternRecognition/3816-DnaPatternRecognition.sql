-- Last updated: 4/20/2026, 1:24:17 PM
# Write your MySQL query statement below
select *,case when dna_sequence like 'ATG%' then 1 else 0 end as has_start,
case when dna_sequence LIKE  ('%TAG')  OR dna_sequence like '%TAA' or dna_sequence like '%TGA'  then 1 else 0 end as has_stop,
case when dna_sequence LIKE ('%ATAT%') then 1 else 0 end as has_atat,
case when dna_sequence like '%GGG%' then 1 else 0 end as has_ggg
 from Samples
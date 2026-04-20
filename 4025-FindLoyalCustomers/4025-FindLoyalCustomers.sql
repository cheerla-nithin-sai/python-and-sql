-- Last updated: 4/20/2026, 1:23:59 PM
# Write your MySQL query statement below
select customer_id from (SELECT customer_id,count(*) as ct,datediff(max(transaction_date),min(transaction_date)) as dt,round(sum(case when transaction_type='refund' then 1 else 0 end)/count(*)*1.0,2) as ref_cnt,sum(case when transaction_type='purchase' then 1 else 0 end) as pur_cnt from customer_transactions
group by customer_id
having dt>=30 and ref_cnt<0.2 and pur_cnt>=3) a
order by customer_id
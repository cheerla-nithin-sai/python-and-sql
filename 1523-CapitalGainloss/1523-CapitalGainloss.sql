-- Last updated: 4/20/2026, 1:26:27 PM
select stock_name,sum(case when operation='buy' then -price else price end) as capital_gain_loss
from stocks
group by stock_name
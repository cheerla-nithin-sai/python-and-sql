-- Last updated: 4/21/2026, 8:41:53 AM
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      with cte as (select salary,dense_rank()over(order by salary desc) as rn
      from Employee)
      select distinct salary from cte
      where rn=N
  );
END
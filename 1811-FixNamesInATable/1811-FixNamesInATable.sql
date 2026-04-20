-- Last updated: 4/20/2026, 1:26:06 PM
# Write your MySQL query statement below
SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LCASE(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;

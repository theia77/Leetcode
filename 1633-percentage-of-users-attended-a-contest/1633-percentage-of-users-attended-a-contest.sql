# Write your MySQL query statement below
SELECT Register.contest_id,ROUND((COUNT(Register.user_id)*100.0/(SELECT COUNT(*) FROM Users)),2) as percentage 
FROM Register JOIN Users 
On Register.user_id=Users.user_id 
GROUP BY Register.contest_id
ORDER BY percentage desc, contest_id asc
# Write your MySQL query statement below
SELECT user_id AS buyer_id, join_date, COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.buyer_id AND YEAR(order_date)='2019'
GROUP BY user_id
ORDER BY user_id

#Most readable:
#From: https://leetcode.com/problems/market-analysis-i/discuss/357761/A-simple-MYSQL-solution-beats-100-so-far
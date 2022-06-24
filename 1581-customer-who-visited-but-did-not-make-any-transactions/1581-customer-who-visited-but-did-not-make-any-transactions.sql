# Write your MySQL query statement below
#I liked this solution the best: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/discuss/865760/Simplest-Just-a-LEFT-JOIN-No-SUB-Query.

#THIS GETS 
SELECT
	customer_id,
	COUNT(Visits.visit_id) AS count_no_trans
FROM
	visits
LEFT JOIN Transactions
	ON Visits.visit_id = Transactions.visit_id
WHERE 
	Transactions.visit_id IS NULL
GROUP BY customer_id
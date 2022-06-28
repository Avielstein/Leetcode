# Write your MySQL query statement below
select customer_number from orders
group by customer_number
order by count(*) desc limit 1;

#super simple solution from: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/discuss/103297/Simple-Solution-using-group-by
# Write your MySQL query statement below


SELECT
    sell_date, #date the number of different products sold and their names.
    COUNT(DISTINCT product) num_sold, #
    GROUP_CONCAT(DISTINCT product) products
FROM activities
GROUP BY sell_date
#ORDER BY sell_date

#The sold products names for each date should be sorted lexicographically.
# Write your MySQL query statement below


SELECT
    sell_date, #date the number of different products sold and their names.
    COUNT(DISTINCT product) num_sold, #
    GROUP_CONCAT(DISTINCT product) products
FROM activities
GROUP BY sell_date 

#Return the result table ordered by sell_date.
ORDER BY sell_date #
#already ordered by sell date, but this will make sure if you have 
#them in a random order, then it will list cronolocally

#where is this taken care of:
#"The sold products names for each date should be sorted lexicographically."?
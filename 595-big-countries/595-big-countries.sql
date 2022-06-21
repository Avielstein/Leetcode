
# Write your MySQL query statement below
/*
Approach I: Using WHERE clause and OR [Accepted]
Intuition

Use WHERE clause in SQL to filter these records and get the target countries.

Algorithm

According to the definition, a big country meets at least one of the following two conditions:

It has an area of bigger than 3 million square km.
It has a population of more than 25 million.
So for the first condition, we can use the following code to get the big countries of this type.
*/
SELECT
    name, population, area
FROM
    world
WHERE
    area >= 3000000 OR population >= 25000000
;
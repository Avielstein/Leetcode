# Write your MySQL query statement below
SELECT MAX(salary) 
AS SecondHighestSalary #rename the header
FROM Employee 
WHERE salary NOT IN ( SELECT MAX(salary) 
                   FROM Employee
                 );


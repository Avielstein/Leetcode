# Write your MySQL query statement below

#topic of interst
SELECT T.employee_id

#data of interest
FROM
    #Right join + left join
    (SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
     UNION 
     SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id))
AS T

#A line that has missing information
WHERE T.salary IS NULL OR T.name IS NULL

#sort
ORDER BY employee_id;
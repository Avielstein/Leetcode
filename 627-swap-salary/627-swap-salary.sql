# Write your MySQL query statement below


UPDATE salary
    SET sex  = (CASE WHEN sex = 'm' 
        THEN  'f' 
        ELSE 'm' 
        END)

#alternative use IF, which basically replaces the when, then, else, end and reapalces with commas
#UPDATE Salary SET sex = IF(sex='f', 'm', 'f');
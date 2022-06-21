# Write your MySQL query statement below

#resources:
#get first character in a string (too eleminate M )
#https://stackoverflow.com/questions/792294/how-to-get-first-character-of-a-string-in-sql

#how to tell if its even or odd using modulo 
#https://tableplus.com/blog/2019/09/select-rows-odd-even-value.html#:~:text=Syntax,otherwise%2C%20that's%20an%20odd%20number.
/*
select
    employee_id, name, salary
from
    Employees
where
    left(name, 1) <> 'M'  and employee_id % 2 = 1
;
*/

SELECT employee_id, 
    CASE 
    WHEN employee_id %2=1 AND name NOT LIKE 'M%' THEN salary 
    ELSE 0 
    END 
AS bonus FROM Employees


ORDER BY employee_id

;


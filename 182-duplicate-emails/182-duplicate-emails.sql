# Write your MySQL query statement below
#this works took, probs slightly cleaner
/*
Select Email
From Person
GROUP BY Email
Having count(Email)>1
*/

SELECT DISTINCT a.Email
  FROM Person AS a , Person AS b
    WHERE a.Id <> b.Id AND a.Email = b.Email
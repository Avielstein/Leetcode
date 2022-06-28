# Write your MySQL query statement below
SELECT w1.id
FROM Weather AS w1 , Weather AS w2
#here the are using specialized function "datediff", to find consecutive days
#assumably there is some general diff function that can help us comparing different
#values
WHERE w1.Temperature > w2.Temperature AND DATEDIFF(w1.recordDate , w2.recordDate) = 1
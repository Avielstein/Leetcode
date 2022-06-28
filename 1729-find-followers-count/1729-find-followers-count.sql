# Write your MySQL query statement below


select user_id,
count(distinct(follower_id)) as followers_count
from
followers
group by user_id

#Most readable solution:
#https://leetcode.com/problems/find-followers-count/discuss/1458530/Easy-MySQL-Solution
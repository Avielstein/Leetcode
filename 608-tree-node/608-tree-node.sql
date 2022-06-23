# Write your MySQL query statement below
Select ID as id,

#This is what constructs the output
case
    #when is the same as if, root, inner, leaf, self explainitory
    when P_ID is null then 'Root'
    #the "(select p_id from tree)" get us the list of node number
    when id in (select p_id from Tree) then 'Inner' #
    else 'Leaf'

#set col header
end as type from TREE
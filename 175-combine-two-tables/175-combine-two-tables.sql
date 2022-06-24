# Write your MySQL query statement below
select firstName, lastName, city, state
from Person
left join Address  #has to be left join to keep the nulls from the person dataset
on Person.personId=Address.personId

#https://stackoverflow.com/questions/32400255/mysql-combine-two-tables-by-id
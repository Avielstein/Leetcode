#from https://leetcode.com/problems/sales-person/discuss/104100/No-subquery-simple-select-from-where-with-right-join%3A)
select salesperson.name
from orders o join company c on (o.com_id = c.com_id and c.name = 'RED')
right join salesperson on salesperson.sales_id = o.sales_id
where o.sales_id is null
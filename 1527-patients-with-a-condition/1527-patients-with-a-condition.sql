# Write your MySQL query statement below
select 
    patient_id, patient_name, conditions
from 
    Patients
where 
    #we look for things conditions starting with "DIAB1"
    #which can either be at the begingin of the list
    #or in the middle
    conditions LIKE 'DIAB1%' or conditions LIKE '% DIAB1%' 

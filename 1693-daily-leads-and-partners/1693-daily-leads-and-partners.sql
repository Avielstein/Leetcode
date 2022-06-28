

SELECT date_id, make_name, 
COUNT(DISTINCT lead_id) AS unique_leads, 
COUNT(DISTINCT partner_id) AS unique_partners

FROM DailySales
GROUP BY 1, 2 #sort by two things at once, very cool 

#made a bit more readable, IMO
#from: https://leetcode.com/problems/daily-leads-and-partners/discuss/976703/Simple-MySQL-solution-using-COUNT-DISTINCT
-- 코드를 작성해주세요
select ROUTE,
CONCAT(round(sum(d_between_dist),1),"km") as TOTAL_DISTANCE, 
CONCAT(round(avg(d_between_dist),2) ,'km') as AVERAGE_DISTANCE
from subway_distance
group by route
order by round(sum(d_between_dist),1) desc;
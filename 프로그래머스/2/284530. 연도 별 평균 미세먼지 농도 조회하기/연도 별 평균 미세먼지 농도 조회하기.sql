-- 코드를 작성해주세요
select YEAR(YM) AS YEAR , ROUND(AVG(PM_VAL1),2) AS PM10 ,ROUND(AVG(PM_VAL2),2) AS 'PM2.5'
from AIR_POLLUTION
WHERE LOCATION2 LIKE '%수원%'
GROUP BY YEAR(YM)
ORDER BY YEAR(YM) ASC;
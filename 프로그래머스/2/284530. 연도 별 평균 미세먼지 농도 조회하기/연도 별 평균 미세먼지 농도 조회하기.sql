select year(ym) as 'year', round(avg(pm_val1),2), round(avg(pm_val2),2)
from air_pollution
where location1 = '경기도' and location2 = '수원'
group by year(ym)
order by year(ym) asc
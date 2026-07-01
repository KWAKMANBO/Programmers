select year, m - e.size_of_colony as year_dev, e.id  
from ecoli_data e 
join 
(
    select 
        year(DIFFERENTIATION_DATE) as year, 
        max(size_of_colony) as m
    from ecoli_data
    group by year(DIFFERENTIATION_DATE)
) as y on year(e.DIFFERENTIATION_DATE) = y.year
order by year(DIFFERENTIATION_DATE) asc, year_dev asc 
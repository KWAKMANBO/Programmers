select history_id, car_id, 
start_date,end_date,
case 
    when datediff(end_date, start_date) + 1 < 30 then '단기 대여'
    else '장기 대여'
end as rent_type
from car_rental_company_rental_history
where start_date like '2022-09-%'
order by history_id desc 
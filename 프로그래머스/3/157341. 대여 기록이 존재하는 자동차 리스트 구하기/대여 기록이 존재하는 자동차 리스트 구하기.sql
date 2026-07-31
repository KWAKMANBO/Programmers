select ch.car_id
from car_rental_company_car cr join car_rental_company_rental_history ch on cr.car_id = ch.car_id
where cr.car_type = '세단' and month(start_date) = 10
group by car_id
order by ch.car_id desc
select car_id, 
    case 
        when car_id in 
        (
            # 2022년 10월 16일에 대여중인 자동차의 car_id를 조회하는 쿼리문
            select car_id
            from car_rental_company_rental_history
            where '2022-10-16' between start_date and end_date
        ) then '대여중'
    else
        '대여 가능'
    end as availability
from car_rental_company_rental_history
group by car_id
order by car_id desc






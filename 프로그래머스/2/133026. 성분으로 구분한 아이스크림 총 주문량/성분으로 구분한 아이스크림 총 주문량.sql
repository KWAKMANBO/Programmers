select ingredient_type as INGREDEIENT_TYPE,sum(total_order) as TOTAL_ORDER
from first_half f join icecream_info i on f.flavor = i.flavor
group by ingredient_type
order by total_order asc
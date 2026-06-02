select left(product_code,2) as category, count(*)
from product
group by left(product_code, 2)

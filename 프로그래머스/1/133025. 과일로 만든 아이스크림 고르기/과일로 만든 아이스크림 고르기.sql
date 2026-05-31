select ii.flavor
from icecream_info as ii join first_half as fh on ii.flavor = fh.flavor
where 1 
and
fh.TOTAL_ORDER > 3000 
and
ii.ingredient_type = 'fruit_based'
order by fh.total_order desc

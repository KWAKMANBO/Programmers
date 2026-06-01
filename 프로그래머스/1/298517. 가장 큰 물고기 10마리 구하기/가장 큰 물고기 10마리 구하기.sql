select id ,ifnull(length, 10)
from fish_info
order by length desc, id asc
limit 10
select count(*) fish_count, fish_name
from fish_info fi join fish_name_info fn on fi.fish_type = fn.fish_type
group by fi.fish_type
order by fish_count desc
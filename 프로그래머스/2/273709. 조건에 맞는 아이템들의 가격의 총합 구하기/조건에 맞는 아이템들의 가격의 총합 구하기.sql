select sum(price)
from item_info
where rarity='LEGEND'
group by rarity
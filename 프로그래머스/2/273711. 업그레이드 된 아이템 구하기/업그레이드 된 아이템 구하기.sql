select ii.ITEM_ID, ii.ITEM_NAME, ii.RARITY
from 
item_info as ii join item_tree as it 
on 
ii.item_id = it.item_id
where it.parent_item_id in (
    select item_id
    from item_info
    where rarity = 'RARE'
)
order by  ii.item_id desc;
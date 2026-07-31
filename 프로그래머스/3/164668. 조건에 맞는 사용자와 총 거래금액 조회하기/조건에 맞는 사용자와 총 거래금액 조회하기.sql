select ub.writer_id user_id, uu.nickname nickname, sum(price) total_sales
from used_goods_board ub join used_goods_user uu on ub.writer_id = uu.user_id
where ub.status = 'DONE'
group by ub.writer_id
having sum(price) >= 700000
order by sum(price) asc

# select ub.writer_id user_id, uu.nickname nickname, ub.price total_sales
# from used_goods_board ub join used_goods_user uu on ub.writer_id = uu.user_id
# where ub.status = 'DONE' 
# and ub.price >= 700000
# order by ub.price asc 


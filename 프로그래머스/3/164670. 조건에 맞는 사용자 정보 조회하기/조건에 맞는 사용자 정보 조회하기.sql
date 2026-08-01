select uu.user_id, uu.nickname, concat(uu.city, " ", uu.street_address1," ", uu.street_address2) 전체주소,
    concat(substring(uu.tlno,1,3),"-", substring(uu.tlno,4,4),"-", substring(uu.tlno,8,4) ) 전화번호
from used_goods_user uu join used_goods_board ub on uu.user_id = ub.writer_id
group by uu.user_id
having count(*) >= 3
order by uu.user_id desc


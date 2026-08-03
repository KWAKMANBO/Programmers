select concat('/home/grep/src/', ub.board_id,'/',uf.file_id,uf.file_name,uf.file_ext) file_path
from used_goods_board ub join used_goods_file uf on  ub.board_id = uf.board_id
where ub.board_id = (select board_id
                   from used_goods_board
                     order by views desc
                     limit 1
                    )
order by  views desc, uf.file_id desc


                    
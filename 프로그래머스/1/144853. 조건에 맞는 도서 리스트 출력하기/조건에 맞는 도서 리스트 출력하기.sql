select book_id, published_date
from book
where 1 and published_date like '2021%' and category = '인문'
order by published_date asc
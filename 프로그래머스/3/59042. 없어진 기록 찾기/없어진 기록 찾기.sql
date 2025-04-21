-- 코드를 입력하세요
select ao.animal_id as ANIMAL_ID, ao.name as NAME
from animal_ins as ai right join animal_outs as ao on ai.animal_id = ao.animal_id
where ai.animal_id is null

-- 코드를 작성해주세요
select hd.DEPT_ID, hd.DEPT_NAME_EN, round(avg(he.sal),0) as AVG_SAL
from hr_department as hd join hr_employees as he on hd.dept_id = he.dept_id
group by dept_id
order by avg(he.sal) desc;
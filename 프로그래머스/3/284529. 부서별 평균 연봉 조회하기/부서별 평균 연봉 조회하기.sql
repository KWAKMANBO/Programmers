select he.dept_id dept_id, hd.dept_name_en dept_name_en, round(avg(sal),0) avg_sal
from hr_department hd join hr_employees he on hd.dept_id = he.dept_id
group by he.dept_id
order by avg_sal desc

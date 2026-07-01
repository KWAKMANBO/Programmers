select sum(hg.score) score, he.emp_no, he.emp_name, he.position, he.email
from 
    hr_department hd join hr_employees he on hd.dept_id = he.dept_id 
    join hr_grade hg on he.emp_no = hg.emp_no
# where he.position = '팀원'
group by he.emp_no
order by score desc
limit 1



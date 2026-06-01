select count(*) as count
from ecoli_data
where 1=1
and
genotype & 2 != 2
and 
(genotype & 1 = 1 or genotype & 4 = 4)


# SELECT COUNT(*) AS COUNT
# FROM ECOLI_DATA A
# WHERE 1=1
#   AND (GENOTYPE & 2) != 2
#   AND ((GENOTYPE & 4) = 4 OR (GENOTYPE & 1) = 1);
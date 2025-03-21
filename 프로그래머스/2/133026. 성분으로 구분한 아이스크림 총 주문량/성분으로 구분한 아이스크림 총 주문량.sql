-- 코드를 입력하세요
# SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
# FROM FIRST_HALF AS F INNER JOIN ICECREAM_INFO AS I ON F.FLAVOR = I.FLAVOR
# GROUP BY F.INGREDIENT_TYPE
# ORDER BY SUM(TOTAL_ORDER) ASC;
SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER)  AS TOTAL_ORDER 
FROM FIRST_HALF AS F
JOIN
ICECREAM_INFO AS I
ON 
F.FLAVOR = I.FLAVOR
GROUP BY I.INGREDIENT_TYPE
ORDER BY F.TOTAL_ORDER
;
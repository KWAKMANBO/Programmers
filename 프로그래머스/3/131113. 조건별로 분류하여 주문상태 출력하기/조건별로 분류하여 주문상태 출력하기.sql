-- 코드를 입력하세요
SELECT F.ORDER_ID, F.PRODUCT_ID, DATE_FORMAT(F.OUT_DATE, '%Y-%m-%d') AS OUT_DATE, 
CASE 
WHEN DATE_FORMAT(OUT_DATE, '%Y-%m-%d') <= '2022-05-01' THEN '출고완료'
WHEN DATE_FORMAT(OUT_DATE, '%Y-%m-%d') > '2022-05-01' THEN '출고대기'
ELSE '출고미정' END AS '출고여부'
FROM FOOD_ORDER AS F
ORDER BY ORDER_ID ASC;

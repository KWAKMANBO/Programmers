SELECT FLOOR(PRICE/10000)*10000 AS PRICE_GROUPS, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUPS
ORDER BY PRICE_GROUPS ASC;
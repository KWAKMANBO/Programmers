-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO AS F JOIN FISH_NAME_INFO AS FN ON F.FISH_TYPE = FN.FISH_TYPE
WHERE FN.FISH_NAME IN ('BASS','SNAPPER')
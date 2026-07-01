-- 1. 0부터 23까지의 가상 시간 도표(hour_list) 생성
WITH RECURSIVE hour_list AS (
    SELECT 0 AS hour                    -- 시작점: 0시
    UNION ALL
    SELECT hour + 1 FROM hour_list WHERE hour < 23 -- 반복: 23시까지 1씩 증가
)

-- 2. 가상 도표를 기준으로 실제 데이터 결합 및 집계
SELECT 
    h.hour AS HOUR, 
    COUNT(a.animal_id) AS COUNT        -- 빈 시간대는 0으로 처리하기 위해 id 카운트
FROM hour_list h
LEFT JOIN animal_outs a ON h.hour = HOUR(a.datetime) -- 가상 시간과 실제 데이터 시간 매칭
GROUP BY h.hour                        -- 시간대별로 그룹화
ORDER BY h.hour;                       -- 0시부터 오름차순 정렬
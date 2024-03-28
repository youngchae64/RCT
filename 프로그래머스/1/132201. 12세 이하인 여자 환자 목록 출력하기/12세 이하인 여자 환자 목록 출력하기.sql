SELECT 
    PT_NAME, 
    PT_NO, -- 전화번호가 NULL인 경우 'NONE'으로 대체
    GEND_CD, 
    AGE,
    COALESCE(TLNO,'NONE') AS TLNO
FROM 
    PATIENT
WHERE 
    AGE <= 12 AND GEND_CD = 'W'  -- 나이가 12 이하이고 성별 코드가 'W'인 환자 선택
ORDER BY 
    AGE DESC,    -- 나이를 기준으로 내림차순 정렬
    PT_NAME ASC; -- 나이가 같을 경우 환자 이름을 기준으로 오름차순 정렬

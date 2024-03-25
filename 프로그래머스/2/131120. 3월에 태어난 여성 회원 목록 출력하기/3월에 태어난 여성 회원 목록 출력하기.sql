-- 코드를 입력하세요

#생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일 조회하는 문장 
#TLNO가 NULL인 경우 출력 대상에서 제외, 결과는 회원 ID를 기준으로 오름차순 정렬하기 

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE 
WHERE MONTH(DATE_OF_BIRTH) = 3
        AND TLNO IS NOT NULL
        AND GENDER = 'W'
ORDER BY MEMBER_ID;

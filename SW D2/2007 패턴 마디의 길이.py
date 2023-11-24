T = int(input())  # 테스트 케이스의 개수를 입력 받음

# 각 테스트 케이스에 대해 반복
for test_case in range(1, T + 1):
    s = input()  # 길이가 30인 문자열 입력 받음
    period = 1  # 초기 마디 길이를 1로 설정
    
    # 마디의 길이를 1부터 최대 10까지 검사
    for i in range(1, 11):
        # 문자열을 i 길이만큼 잘라서 첫 마디와 나머지 부분을 비교
        if s[:i] == s[i:i*2]:
            period = i  # 만약 일치하면 마디 길이를 업데이트
            break  # 반복 중지
    
    print(f'#{test_case} {period}')

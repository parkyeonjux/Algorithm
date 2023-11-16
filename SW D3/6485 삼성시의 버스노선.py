import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnts = [0]*5001 #0부터 시작하니까 버스 번호에 맞춰서 배열 정의
    for _ in range(N):  #N회 반복
        S, E = map(int, input().split())
        for i in range(S, E+1):
            cnts[i] += 1
    P = int(input())
    sols =[]
    for _ in range(P):
        t = int(input())
        sols.append(cnts[t])
    print(f'#{test_case}', *sols)
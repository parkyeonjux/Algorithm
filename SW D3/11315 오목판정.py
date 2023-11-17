#함수 작성 다중루프는 별도의 함수를 만들어서 탈출하기 
def solve():
    for si in range(N):
        for sj in range(N): #모든 좌표 순회
            for di,dj in ((0,1), (1,0), (1,1), (-1,1)):
                for mul in range(5):
                    ni, nj = si+di*mul, sj+dj*mul 
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]=='o':
                        pass
                    else:
                        break
                else:
                    return 'YES'
    return 'NO'            
              
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) 
    arr = [input() for _ in range(N) ]
    ans = solve() 
    print(f'#{test_case} {ans}')

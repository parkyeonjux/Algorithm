T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        mx = lst[i-2]
        for j in range(i-1, i+3):
            if i == j:
                continue
            else:
                if mx < lst[j]:
                    mx = lst[j]
        if lst[i] > mx:
            ans += lst[i]-mx
    print(f'#{test_case} {ans}')



    #다른풀이 

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        mx = max(lst[i-2:i] + lst[i+1:i+3])  #슬라이싱으로 max 쓰기 
           
        if lst[i] > mx:
            ans += lst[i]-mx
    print(f'#{test_case} {ans}')
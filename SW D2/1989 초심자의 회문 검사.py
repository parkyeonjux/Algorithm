T = int(input()) 
for test_case in range(1, T+1): 
   
    s = list(input())    
    s_1 = s[::-1]
    if s == s_1: 
    	answer = 1
    else:
        answer = 0
    
   
    print("#%d" % test_case, answer)
   # print(f'#{test_case} {answer}')
    

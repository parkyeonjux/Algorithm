T = int(input()) 
for test_case in range(1, T+1): 
    n = list(map(int, input().split())) 
    print("#%d %d" % (test_case, round( (sum(n)-max(n)-min(n))/8)) )

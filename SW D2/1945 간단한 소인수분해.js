/*
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
divs = [2, 3, 5, 7, 11]   #여러번 잡히면 밖에 쓰기 계속 돌면서 잡히니까
for test_case in range(1, T+1):
    N = int(input())
    cnts = [0]*5
    for i in range(5):
        while N % divs[i] ==0:
            cnts[i] += 1
            N //= divs[i]

    print(f'#{test_case}', *cnts) 
    */
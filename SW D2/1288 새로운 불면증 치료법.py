T=int(input())

for test_case in range(1,T+1):
    number=[0,1,2,3,4,5,6,7,8,9]
    #xN번에서 x를 찾기위해 flag를 씀
    flag=1
    n=int(input())
    tmp=n
    
    #첫 번째 while문은 0~9까지의 모든 숫자가 나왔는지 확인하기 위해서
    while len(number)!=0:
        #두 번째 while문은 숫자를 한자리씩 자르기 위함
        while tmp!=0:
            na = tmp%10
            tmp//=10
            #나머지가 number배열안에 있으면 삭제
            if na in number:
                number.remove(na)
        #숫자를 한자리씩 다 확인하고 나면
        #xN배를 위해 flag를 하나 올려줌
        flag+=1
        #tmp값을 x배 해서 위의 과정 반복
        tmp=n*flag

    print("#%d %d" % (test_case, (flag-1)*n))

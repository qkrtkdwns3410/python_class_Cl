#함수의 반환값
def func_sum(x1, x2) :
    tot = 0
    for i in range(x1, x2+1) :
        tot += i
        #해석 : 인자 x1,x2까지의 숫자를 tot에 더한다. 숫자 1 4 를 입력시 1,2,3,4 을 더한 값이 tot에 저장됩니다.

    return(tot)
    #return 문으로 함수입력시 해당 결과값이 반환됩니다. 해당값은 print로 출력해야 결과값이 보이게됩니다.
print(func_sum(1,4))
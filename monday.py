#
''''
if 조건문 :
            명령문
            명령문
            같은 조건의 명령문에서는 같은 들여쓰기를 할 것( 매우 중요)
            한줄로 쓰는경우 ;을 이용해 구분할것  

'''''
score=85
print("[결과]")
if score>=60:

    result = "A"

elif score>=50:
    result = "B"
else :
    result = "C"
print("%d점은 %s입니다." % (score, result))

a=1
while a <=200 :
    if a%7==0 and a%5!=0 :
        if a==196 :
            print(a)
            a += 1
        else :
            print(a, end=",")
            a +=1
    else : a += 1



n= 100
while 100 <= n <=300:
    a= n//100
    b= n%100
    c= b//10
    d= b%10
    if a%2==0 and c%2==0 and d%2==0 :
        if n==288:
            print(n)
        else:
            print(n,end=",")
        n +=1
    else : n+=1









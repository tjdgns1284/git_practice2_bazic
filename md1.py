#1 약수 구하기
a=int(input())
b= 1
while a>=b :
    if (a%b) == 0:
        print("%d(은)는 %d의 약수입니다." % (b,a))
        b += 1
    else:
        b += 1

#2 약수 구하고 소수 나타 내기
a = int(input())
b = 1
counter = 0
while a >= b:
    if (a % b) == 0:
        print("%d(은)는 %d의 약수입니다." % (b,a))
        b += 1
        counter += 1
    else:
        b += 1
if counter == 2:
    print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." % (a, a))

# 3 대소문자 구문
a = input()
if str("z") >= a >= str("a") :
    print("%s 는 소문자 입니다." % a)
elif str("Z") >= a >= str("A") :
    print("%s 는 대문자 입니다." % a)
else :
    print("%s 는 알파벳이 아닙니다." % a)


# 4 가위바위보
a = ["가위", "바위", "보"]
M1 = input(a)
M2 = input(a)
if not( M1 and M2 in a) :
    print("잘못된 입력입니다.")
elif M1 == M2 :
    print("Result : Draw!")
elif (M1 == "가위" and M2 == "보") or (M1 == "바위" and M2 == "가위") or (M1 == "보" and M2 == "바위") :
    print("Result : Man1 Win!")
elif (M1 == "바위" and M2 == "보") or (M1 == "가위" and M2 == "바위") or (M1 == "보" and M2 == "가위") :
    print("Result : Man2 Win!")

#5 ASCII 코드 대소문자 변환
#
'''
ord(문자) -> 해당문자의 아스키 코드 값을 불러옴 
%c 문자 %s 문자열 %f 실수 %d 십진수 %x 16진수 %o 8진수 %b 2진수 
'''
a=input()
if 123> ord(a) > 96 :
    b= ord(a) -32

    print("%s(ASCII: %d) => %c(ASCII: %d)" % (a, ord(a), b, b))
elif 91>ord(a)>64 :
    b = ord(a) +32

    print("%s(ASCII: %d) => %c(ASCII: %d)" % (a, ord(a), b, b))
else :
    print("%s" % a)

#6 1~200 에서 7의 배수이지만 5의 배수는 아닌것 찾기

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


#7 100~300사이의 모든 자리수가 짝수인수
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

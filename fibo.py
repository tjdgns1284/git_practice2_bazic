lst= [1, 2, 3]
print(type(lst))
Var1 = 10
Var2 = 10
print(Var1 is Var2)


obj = None

if obj:
    print("obj는 None이 아니다.")
else:
    print("obj는 None 이다")

x= y= 10
x,y= 10, 20
print("%d" % x)
print("%d" % y)
del(x)
del(y)
print("%d" % x)
print("%d" % y)

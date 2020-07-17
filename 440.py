print("안녕하세요.\n 파이선\n 프로그래밍")
print("""
    안녕하세요
    파이선
    프로그래밍
    """)
print("큰따옴표 \" 를 출력합니다")
print('작은따옴표 \'를 출력합니다')
print(" 싸\n 피\n 4기\n 화\t 이\t 팅\t")
print("이름: %s" % "황성훈")
print("나이: %s 세" % "28")
print("결혼 : %s" % False)
print("이름 : %(name)s \n 나이 : %(age)s세 \n 결혼 : %(ruf)s" % {"name": "tom", "age": "28", "ruf":False})

print("%c = %d" % (97, 97))
print("%c %d %o %x" % (89, 89, 89, 89))
print("%s %d %x" % ("가", ord("가"), ord("가")))
print("%010.2f %d" % (3.141592, 3.14))
print("이름: {1} \n 나이: {0}" .format("황성훈", 28))
print("%05f 점은 상위%.5f%%에 해당합니다 " % (99.1415192, 0.52151))
print("{0:f}\t{1:.2f}".format(3.14, 3.14))
print("{0:*^11}" .format("가운데정렬"))
print("{0:050.5f}" .format(3.141592))



try:
    score = int(input("请输入分数："))
except ValueError:
    print("输入不正确，请重新输入")
else:
    if not 0<=score<=100:
        print("输入的分数不在0-100之间，请重新输入")
    elif score >= 90:
        print("优秀")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")
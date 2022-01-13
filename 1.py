for num in range(1,101):
    if num % 3 == 0 and num % 15 != 0:
        print("勉強したい")
    elif num % 5 == 0 and num % 15 != 0:
        print("就活したい")
    elif num % 3 == 0 and num % 5 == 0:
        print("だいがく爆破したい")
    else:
        print(num)



    
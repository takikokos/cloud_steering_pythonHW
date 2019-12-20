def eval_data():
    try:
        inp = input()
        if inp == "cancel":
            print("Bye!")
            return
        x = int(inp)
    except:
        print("Не удалось преобразовать введенный текст в число.")
        eval_data()
    else:
        if x % 2 == 0:
            print(x // 2)
        else:
            print(x * 3 + 1)
        eval_data()
    finally:
        return

eval_data()
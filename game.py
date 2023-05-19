#!/usr/bin/python

loc = 0
ticket = 0
gameover = 0

print("あなたはOIT梅田タワーにやってきた。空腹なので何とか食事がしたい。")
print("(入力はすべて日本語か英語の動詞1語で行ってください。)")
while gameover == 0:

# 状況説明
    if loc == 0:
        print("OIT梅田タワーの前にいる。")
    elif loc == 1:
        print("エントランスホールにいる。")
    elif loc == 2:
        print("エレベータの中にいる。エレベータは1Fにいるようだ。")
    elif loc == 3:
        print("21Fレストランにいる。")

    print("どうする?")
    cmd = input()
    if loc == 0:
        if cmd == "見る" or cmd == "look":
            print("都市型のタワーキャンパスだ。")
        elif cmd == "入る" or cmd == "enter":
            print("中に入ろう。")
            loc = 1
        else:
            print("それはできません。")

    elif loc == 1:
        if cmd == "見る" or cmd == "look":
            print("エレベータとセキュリティゲートと受付がある。受付には人がいる。")
        elif cmd == "話す" or cmd == "talk":
            print("受付『学外の方はゲート内に入れません。』")
        elif cmd == "入る" or cmd == "enter":
            print("ゲートが開かなくて入れない。")
        elif cmd == "乗る" or cmd == "使う" or cmd == "use":
            print("エレベータに乗り込んだ。")
            loc = 2
        elif cmd == "出る" or cmd == "exit":
            print("外に出よう。")
            loc = 0
        else:
            print("それはできません。")

    elif loc == 2:
        if cmd == "見る" or cmd == "look":
            print("21階のボタンを押すことができそうだ。")
        elif cmd == "押す" or cmd == "push":
            print("エレベータが上昇して21階についた。")
            loc = 3
        elif cmd == "出る" or cmd == "exit":
            print("エレベータを出た。")
            loc = 1
        else:
            print("それはできません。")
    elif loc == 3:
        if cmd == "見る" or cmd == "look":
            print("食べ物が食べられそうだ。スタッフがいる。")
        elif cmd == "話す" or cmd == "talk":
            print("スタッフ『600円で食券をお買い求めください。』")
        elif cmd == "入る" or cmd == "enter":
            print("もうレストランの中にいる。")
        elif cmd == "乗る" or cmd == "使う" or cmd == "出る" or cmd == "use":
            print("エレベータに乗り込んだ。エレベータは下降した。")
            loc = 2
        elif cmd == "食べる" or cmd == "eat":
            if ticket == 0:
                print("無銭飲食をしてはダメだ。")
            else:
                print("お腹が一杯になった！！")
                print("CONGRATURATION! (game end)")
                gameover = 1
        elif cmd == "買う" or cmd == "buy":
            print("食券を買った。")
            ticket = 1
        elif cmd == "出る" or cmd == "exit":
            print("外に出よう。")
            loc = 0
        else:
            print("それはできません。")

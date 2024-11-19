import random as rd

while True:
    print("游戏开始！")
    player_choice = input("请输入你的选择：")
    computer_choice = rd.choice(['剪刀','石头','布'])

    if player_choice == computer_choice:
        print(f"电脑出的是{computer_choice},你出的是{player_choice},平局")
    elif (player_choice == '剪刀' and computer_choice == '布') \
            or (player_choice == '石头' and computer_choice == '剪刀') \
            or (player_choice == '布' and computer_choice == '石头'):
        print(f"电脑出的是{computer_choice},你出的是{player_choice},恭喜你赢了")
    else:
        print(f"电脑出的是{computer_choice},你出的是{player_choice},很遗憾，你输了")

    play_again = input("是否继续游戏？（是/否）")
    if play_again!= '是':
        print("再见！")
        break

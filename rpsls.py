"""
程序目标:通过自定义函数，实现RPSLS游戏。
程序作者:土木四班曾理
"""
import random
def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
     player_number=0
    elif name == "史波克":
         player_number= 1
    elif name == "布":
         player_number= 2
    elif name == "蜥蜴":
         player_number= 3
    elif name == "剪刀":
         player_number= 4
    else:
        print("Error:No Correct Name")
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number == 0:
       comp_name = "石头"
    elif number == 1:
         comp_name = "史波克"
    elif number == 2:
         comp_name = "布"
    elif number == 3:
         comp_name = "蜥蜴"
    elif number == 4:
         comp_name = "剪刀"
    print("计算机的选择为", comp_name)
    return comp_name


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    player_number = name_to_number(player_choice)
    print("您的选择为", player_choice)
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    if (player_number == 0 and comp_number == 3) or (player_number == 0 and comp_number == 4) or (
            player_number == 1 and comp_number == 0) or (player_number == 1 and comp_number == 4) or (
            player_number == 2 and comp_number == 0) or (player_number == 2 and comp_number == 1) or (
            player_number == 3 and comp_number == 1) or (player_number == 3 and comp_number == 2) or (
            player_number == 4 and comp_number == 2) or (player_number == 4 and comp_number == 3):
        print("您赢了")
    elif (player_number == 0 and comp_number == 0) or (player_number == 1 and comp_number == 1) or (
            player_number == 2 and comp_number == 2) or (player_number == 3 and comp_number == 3) or (
            player_number == 4 and comp_number == 4):
        print("您和计算机出的一样呢")
    else:
        print("计算机赢了")


print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name = input()
rpsls(choice_name)
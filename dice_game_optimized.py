"""
投骰子赌大小游戏 - 优化版本

优化点:
1. 简化 bet() 函数的嵌套条件判断,使用逻辑表达式减少代码重复
2. 添加欢迎信息和输入验证提示
3. 使用 continue 跳过无效输入,避免浪费骰子
4. 统一在循环末尾检查游戏结束条件,逻辑更清晰
5. 添加 .lower() 增强容错性
"""

from random import randrange

coin_user, coin_bot = 10, 10  # 可以用一个赋值符号分别为多个变量赋值
rounds_of_game = 0

def bet(dice, wager):
    """
    接收两个参数,一个是骰子点数,另一个用户的输入
    
    优化后的判断逻辑:
    - 减少嵌套的 if-elif 结构
    - 使用布尔表达式简化胜负判断
    """
    if dice == 7:
        print(f'The dice is {dice};\nDRAW!\n')
        return 0
    
    # 判断胜负:当 (dice < 7 且猜小) 或 (dice > 7 且猜大) 时获胜
    # 这个逻辑表达式替代了原来嵌套的 if-else 结构
    user_wins = (dice < 7 and wager == 's') or (dice > 7 and wager == 'b')
    
    if user_wins:
        print(f'The dice is {dice};\nYou WIN!\n')
        return 1
    else:
        print(f'The dice is {dice};\nYou LOST!\n')
        return -1

# 添加欢迎信息
print('Welcome to Dice Game! (b=Big, s=Small, q=Quit)')

while True:
    print(f'You: {coin_user}\t Bot: {coin_bot}')
    wager = input("What's your bet? ").lower()  # 转换为小写,增强容错性
    
    if wager == 'q':
        break
    elif wager not in ('b', 's'):
        # 添加输入验证提示,使用 continue 跳过本次循环
        print('Invalid input! Please enter b, s, or q.\n')
        continue  # 不掷骰子,直接开始下一轮输入
    
    # 只有输入有效时才掷骰子(原代码在输入前就生成了随机数)
    dice = randrange(2, 13)
    result = bet(dice, wager)
    coin_user += result
    coin_bot -= result
    rounds_of_game += 1
    
    # 统一在循环末尾检查游戏结束条件(原代码在 if-elif 分支外部检查)
    if coin_user == 0:
        print("Woops, you've LOST ALL, and game over!")
        break
    elif coin_bot == 0:
        print("Woops, the robot's LOST ALL, and game over!")
        break

print(f"You've played {rounds_of_game} rounds.\n")
print(f"You have {coin_user} coins now.\nBye!")

import random

r = random.randint(1, 100)  # 隨機生成1到100之間的數字
count = 0  # 計數器初始化

while True:
    count += 1  # 每次迴圈執行時，計數器加1
    num = input('請輸入數字:')
    num = int(num)  # 將用戶輸入轉換為整數

    if num == r:
        print('你答對了!')
        print('你總共猜了', count, '次')  # 顯示猜的次數
        break  # 正確猜中後結束迴圈
    elif num > r:
        print('正確數字比較小!')
    elif num < r:
        print('正確數字比較大!')

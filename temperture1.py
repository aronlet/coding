c = input("請輸入*攝氏*溫度(.C)=")
c = int(c)

# 計算華氏溫度
f = c * 9/5 + 32

# 輸出華氏溫度
print(f"{c}攝氏度對應的華氏溫度是{f:.3f}度")

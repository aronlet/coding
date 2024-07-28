age = input('輸入年齡:')
age = int(age)

if age < 13:
    print('國小')
elif 13 <= age < 15:
    print('國中')
elif 15 <= age < 18:
    print('高中')
elif 18 <= age < 22:
    print('大學')
else:
    print('拉基大人!')

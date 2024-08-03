driving = input('你有沒有開過車?')
if driving != 'y' and driving != 'n':
	print('你打錯囉!')
    raise SystemExit

age = input('請輸入你的年齡:')
age = int(age)

if driving == 'y':
    if age >=18:
    	print('要小心開車窩!')
    else:
	    print('這樣會被警察抓走窩!')

if driving == "n":
	if age >= 18:
		print('可以去考駕照囉!')
	else:
		print('要繼續保持!')

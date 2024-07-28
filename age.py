driving = input('你有沒有開過車?')
if driving !='y' and driving != 'n':
	print('你打錯了窩!')  
	raise SystemExit


age = input('請問你的年齡?')
age = int(age)


if driving == "y":
	if age >= 18:
	    print('good!')
	else:
	    print('not good')

elif driving =="n":
	if age >= 18:
	    print('你可以考駕照了ㄟ!')
	else:
	    print('不要犯法窩!!')


driving = input('你有沒有開過車:')
if driving !='y' and driving != 'n':
	print('你打錯囉!!')
	raise SystemExit

age = input ('你幾歲:')
age = int(age)

if driving == 'y':
	if age < 18:
		print('壞壞!')
	else:
		print('小心開車!')

if driving == 'n':
	if age < 18:
		print('繼續保持!')
	else:
		print('為甚麼不去考呢??')
import random

start = input('起始直:')
end = input('終值:')
start = int(start)
end = int(end)

r = random.randint(start,end)
count = 0

while True:
	count += 1 #count = count + 1
	num = input('請輸入數字:')
	num = int(num)

	if num == r:
		print('你答對了!')
		print('你已經猜第', count ,'次')
		break
	elif num > r:
		print('正確數字比較小!')
	elif num < r:
		print('正確數字比較大!')
	print('你已經猜第', count ,'次')
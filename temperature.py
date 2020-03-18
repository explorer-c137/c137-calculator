
# only for conversion of celsius to farenheit and vice versa

initial = input('''Would you like to convert from (a)celsius to farenheit
or (b) farenheit to celsius?:''')


n = ' celsius'
m = ' farenheit'

if initial == 'a':
	c = input('enter celsius:')
	x = float(c) * 9/5 + 32
	print(str(x) + str(m))

elif initial == 'b':
	f = input('enter farenheit:')
	y = float(f) - 32 * 5/9
	print(str(y) + str(n))









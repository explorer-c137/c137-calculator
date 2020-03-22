
# pythagorean calculator
import math

print('      /|')
print('     / |')
print('    /  |')
print('c  /   |a')
print('  /    |')
print(' /     |')
print('/______|')
print('    b')



z = input('Do u want to find the value of a , b , or c?:')

if z=='c':
	rightside = input('a:')
	base = input('b:')
	q = math.sqrt(float(rightside)**2 + float(base)**2)
	print(str(q) + ' is the value of c')
elif z=='a':
	base = input('b:')
	hypotenuse = input('c:')
	q = math.sqrt(float(hypotenuse)**2 - float(base)**2)
	print(str(q) + ' is the value of a')
elif z=='b':
	rightside = input('a:')
	hypotenuse = input('c:')
	q = math.sqrt(float(hypotenuse)**2 - float(rightside)**2)
	print(str(q) + ' is the value of b')







# only for conversion of celsius to farenheit and vice versa



c = input("Enter celsius:")

f = input("Enter farenheit:")


print('')
print("1 for converting celsius to farenheit")
print('2 for convertingfarenheit to celsius')
print('')

choice = input('enter choice:') 

if choice == '1':
	print((int(c) * 9/5) + 32)
elif choice == '2':
	print((int(f) - 32) * 5/9)




# Andrew Kavas
# Multiples of 3 and 5


def mult(var):
	count = 0
	for i in range(1,var):
		if float(i % 5) == 0 or float(i % 3) == 0:
			count += i
	return count


def main():
	varb = int(input('Type a number: '))
	print(mult(varb))


main()


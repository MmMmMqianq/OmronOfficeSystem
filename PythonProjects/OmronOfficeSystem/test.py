def a():
	b = 2
	return b

def c():
	d = 3
	return a()

print(c())


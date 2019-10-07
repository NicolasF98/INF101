def fibonacci(index):
	if (index < 0):
		return -1
	elif (index == 0):
		return 0
	elif (index == 1):
		return 1
	else:
		return ((fibonacci(index - 2)) + (fibonacci(index - 1)))

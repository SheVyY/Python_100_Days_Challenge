print("Welcome to FizzBuzz game!")
print("Starting now")
print("-" * 40)

for number in range(1, 101):
	if number % 3 == 0 and number % 5 == 0:
		print("Fizz Buzz")
	elif number % 5 == 0:
		print("Buzz")
	elif number % 3 == 0:
		print("Fizz")
	else:
		print(number)

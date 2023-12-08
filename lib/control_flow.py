#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
        def admin_login(username, password):
    if username == "zaki" and password == 1234:
        print("Access granted")
    else:
        print("Not granted")


admin_login("zaki", 1234)
    pass
    def hows_the_weather(temperature):
    if temperature > 50:
        print("Use an umbrella")
    else:
        
hows_the_weather()


def fizzbuzz(num):
      if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


result = fizzbuzz(15)
print(result)
    # your code here
    pass

def calculator(operation, num1, num2):
    def calculator(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

result = calculator("add", 5, 3)
print(result)

    # your code here
    pass

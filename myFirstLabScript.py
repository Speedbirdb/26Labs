x = input('What\'s your name? ')
print('Hello ' + x + '.')
y = input('What\'s your student ID? ')
print('Your ID is ' + y + '.')

#2nd
def get_float_or_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            return value  
        except ValueError:
            try:
                return float(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")


var1 = get_float_or_integer_input('Enter value for var1')
var2 = get_float_or_integer_input('Enter value for var2')
sum = var1 + var2
diff = abs(var1 - var2)
mul = var1 * var2

print(f"Var1: {var1}\nVar2: {var2}\nSum: {sum}\nDifference: {diff}\nProduct: {mul}")


#3rd
def get_float_input_0_t0_100(prompt):
    while True:
        user_input = input(prompt)
        try:
            number = float(user_input)
            if 0 <= number <= 100:
                return number
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

lab = get_float_input_0_t0_100('Enter ur lab grade : ') * 0.25
mid = get_float_input_0_t0_100('Enter ur midterm grade : ') * 0.35
fin = get_float_input_0_t0_100('Enter ur final grade : ') * 0.4


#4th
print('\n'.join(['*' * i for i in [1, 2, 3, 2, 1]]))





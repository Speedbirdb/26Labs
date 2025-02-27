while True: 
    ihatethiscourse = input("Please enter a number: ")

    if ihatethiscourse.isdigit() and 3<= ihatethiscourse <=9:
        ihatethiscourse = int(ihatethiscourse)
        break
    else:
        print("Input is not a valid number. Please try again.")


for i in range(1, ihatethiscourse + 1):
    print('*' * i)

for i in range(ihatethiscourse - 1, 0, -1):
    print('*' * i)
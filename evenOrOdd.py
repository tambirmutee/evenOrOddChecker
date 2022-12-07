

num = int(input("Enter your starting number: "))

finish = int(input("Enter your ending number: "))

while(num < finish+1):
    print(f'num = {num}')
    if (num % 2 == 0):
        print("This is Even!")
    else:
        print("This is Odd!")
    num += 1
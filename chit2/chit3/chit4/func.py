def check_divisibility(num):
    if num % 5 == 0 and num % 11 == 0:
        print("The number is divisible by 5 and 11.")
    else:
        print("The number is not divisible by 5 and 11.")

# Main program
number = int(input("Enter a number: "))
check_divisibility(number)

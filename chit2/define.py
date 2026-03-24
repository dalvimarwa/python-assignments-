def check_vote(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

# Main program
age = int(input("Enter age: "))
check_vote(age)

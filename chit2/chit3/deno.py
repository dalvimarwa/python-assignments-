try:
    num = float(input("Enter numerator: "))
    den = float(input("Enter denominator: "))

    result = num / den
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")

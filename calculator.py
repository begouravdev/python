exp = -1
total = 0
maxExp = 0
minExp = 0

while exp != 0:
    expValue = input("Enter an exponent (0 to quit): ").strip()
    if (expValue.isdigit()):
        exp = int(expValue)
        if exp != 0:
            total = total + exp
            if (exp > maxExp):
                maxExp = exp
            if (exp < minExp):
                minExp = exp
    else:
        print("Please enter a valid numeric exponent.")
        
print("The total of all exponents entered is:", str(total))
print("The maximum exponent entered is:", str(maxExp))
print("The minimum exponent entered is:", str(minExp))
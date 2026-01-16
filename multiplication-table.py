num = input("What multiplication table would you like? ")
num = int(num)

mx = [(x + 1) * num for x in range(10)]
mx2 = [str(x+1) + " x " + str(num) + " = " + str((x + 1) * num) for x in range(10)]
mx3 = [f'{x+1} x {num} = {(x + 1) * num}' for x in range(10)]
print(mx3)
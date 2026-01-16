# l = []

# for num in range(1, 100):
#     l.append(num)
# print(l)

l = [num for num in range(1, 100)]
evenNumbers = [num for num in l if num % 2 == 0]
print(evenNumbers[-2])


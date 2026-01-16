name = input("Enter your name: ")
age = input("Enter your age: ").strip()

if age == "":
    print("Hello, " + name.title() + "!")
else:
    age = int(age)
    print("Hello, " + name.title() + "!", " you will be 100 years old in " + str(2024 - age + 100) + ".")


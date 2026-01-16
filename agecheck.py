name = input("Enter your name: ")
age = input("Enter your age: ").strip()

# Check if age is in numeric format
if age.isdigit():
    age = int(age)
    if age < 18:
        print("Hello, " + name.title() + "! You are a minor.")
    else:
        print("Hello, " + name.title() + "! You are an adult.")
else:
    print("Hello, " + name.title() + "!")
    


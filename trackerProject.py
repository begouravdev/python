from datetime import date
import csv

# def days_until(target_date):
#     today = date.today()
#     delta = target_date - today
#     return delta.days

# if __name__ == "__main__":
#     target = date(2026, 1, 31)  # Example target date
#     days_left = days_until(target)
#     print(f"Days until {target}: {days_left} days")
    
    
exp = []
stopped = False

filename = "test.csv"
with open(filename, 'a', newline='') as file:
    csvwriter = csv.writer(file)
    while not stopped:
        xp = int(input ("What is the expense (type 0 to stop): "))
        if xp == 0:
            stopped = True
        else:
            exp.append((date.today().strftime("%Y-%m-%d"), xp))
            csvwriter.writerow([date.today().strftime("%Y-%m-%d"), xp])
file.close()
    
import random
while True:
    try:
        x = int(input("Enter an integer from 10 to 20: "))
        if 10 <= x <= 20:
            break
        else:
            print("Invalid input. Try again.")
    except ValueError:
        print("Invalid data type. Try again.")

random_list = []
for i in range(0, x):
    r = random.randint(1, 100)
    random_list.append(r)
print("The random list:", random_list)

sum = 0
for i in range(0, len(random_list)):
    if random_list[i] % 2 == 0:
        sum += random_list[i]

print("The sum of the even numbers is", sum)



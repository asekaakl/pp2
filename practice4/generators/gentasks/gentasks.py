#task1
def square_generator(n):
    for i in range(n + 1):
        yield i ** 2
for num in square_generator(5):
    print(num)


#task2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))

result = ",".join(str(num) for num in even_numbers(n))
print(result)

#task3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))

for num in divisible_by_3_and_4(n):
    print(num)

#task4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
for num in squares(3, 7):
    print(num)

#task5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num)

"""python的break和continue以及pass"""

for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            print(i, 'equals', j, '*', i // j)
            break
    else:
        print(i, 'is a prime number')

#continue
for num in range(2, 10):
    if num % 2 ==0:
        print("Found an even number", num)
        continue
    print("Found a number", num)
#以下这几种都可以用到pass
# while True:
#     pass

# class ABC:
#     pass

# def log(*args):
#     pass
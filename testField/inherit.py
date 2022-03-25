from testField.gcf import gcf
from testField.change import change
from testField.prime import prime
from testField.fib import fib

print("=======")
print("Greatest multiple: ", gcf(69, 420))

print("=======")
print("Change")
coins = change(41)
print("Q: ", coins[0], "\nD: ", coins[1], "\nN: ", coins[2], "\nP: ", coins[3], "\nT: ", sum(coins))

print("=======")
for i in range(2, 10):
    if prime(i):
        print(i)


print("=======")
print(fib(5))

n = int(input("Podaj liczbę\n"))

numbers = [0,1]

def fib (numbers):
    new = 0
    for i in range(n):
        new = numbers[-1] + numbers[-2]
        numbers.append(new)
        print(new)


fib(numbers)
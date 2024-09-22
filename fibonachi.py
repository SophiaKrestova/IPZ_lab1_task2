def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(0, n):
        next_fib = fib_sequence[i] + fib_sequence[i-1]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

n = int(input("Введіть кількість чисел Фібоначчі, які потрібно вивести: "))
fib_sequence = fibonacci(n)
print(f"Перші {n} чисел Фібоначчі: {fib_sequence}")

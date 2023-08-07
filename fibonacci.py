def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence

# Teste da sequência de Fibonacci
num_terms = int(input("Digite o número de termos da sequência de Fibonacci: "))
resultado = fibonacci(num_terms)
print("Sequência de Fibonacci:", resultado)

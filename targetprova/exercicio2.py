# 2) Verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero or numero == 0

numero_teste = 21  # Altere para testar outro número
if pertence_fibonacci(numero_teste):
    print(f"2) O número {numero_teste} pertence à sequência de Fibonacci.")
else:
    print(f"2) O número {numero_teste} NÃO pertence à sequência de Fibonacci.")

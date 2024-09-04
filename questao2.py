""" 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. """
def questao_2(n):
    i, k = 0, 1

    while i <= n:    
        if i == n:
            return True
        i, k = k, i + k

    return False

number = int(input("Digite um número: "))

if questao_2(number):
    print(f"O número {number} está na sequência de Fibonacci.")
else:
    print(f"O número {number} não está na sequência de Fibonacci.")
""" 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA? """

def calcular_soma(indice):
    soma = 0
    k = 0

    while k < indice:
        k += 1
        soma += k

    return soma

# Valor do índice
indice = 13
resultado = calcular_soma(indice)
print(f"O valor da variável SOMA é {resultado}")

import json

# Função para calcular os valores desejados
def analisar_faturamento(dados):
    # Ler o arquivo JSON
    with open(dados, 'r') as file:
        dados = json.load(file)

    # Extrair os valores de faturamento
    faturamentos = [item['valor'] for item in dados if item['valor'] > 0]

    # Calcular menor e maior valor de faturamento
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    # Calcular a média mensal
    media_mensal = sum(faturamentos) / len(faturamentos)

    # Calcular o número de dias com faturamento superior à média mensal
    dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media


# Chamar a função e imprimir os resultados
menor_faturamento, maior_faturamento, dias_acima_da_media = analisar_faturamento("dados.json")
print(f"Menor faturamento:R${menor_faturamento:.2f}")
print(f"Maior faturamento:R${maior_faturamento:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_da_media}")
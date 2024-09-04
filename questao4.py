""" 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.   """
def converter_valores(valores):
    """Converte valores com vírgula como separador decimal para ponto."""
    valores_convertidos = {}
    for estado, valor in valores.items():
        valor_convertido = float(valor.replace('.', '').replace(',', '.'))
        valores_convertidos[estado] = valor_convertido
    return valores_convertidos

def calcular_porcentagem(faturamento):
    if faturamento:
        total_faturamento = sum(faturamento.values())
        
        if total_faturamento == 0:
            print("Valores inválidos!")
            return
        
        print("Faturamento em porcentagem: ")
        
        for estado, faturamento in faturamento.items():
            porcentagem = (faturamento / total_faturamento) * 100
            print(f"{estado} faturamento: R${faturamento:.2f} porcentagem: {porcentagem:.2f}%")
            
        else:
            print("Error")
            
faturamentos_estados = {
    "SP": "67.836,43",
    "RJ": "36.678,66",
    "MG": "29.229,88",
    "ES": "27.165,48",
    "OUTROS": "19.849,53"
}

faturamento_estados_convertidos = converter_valores(faturamentos_estados)

calcular_porcentagem(faturamento_estados_convertidos)
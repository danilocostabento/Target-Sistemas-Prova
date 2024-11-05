# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

import matplotlib.pyplot as plt

def calcular_percentuais_estado(dados_vendas):
    total_vendas = sum(dados_vendas.values())
    percentuais = {}
    for estado, vendas in dados_vendas.items():
        percentuais[estado] = (vendas / total_vendas) * 100
    return percentuais


if __name__ == "__main__":
    dados_vendas = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53,
    }

    percentuais_estado = calcular_percentuais_estado(dados_vendas)

    for estado, percentual in percentuais_estado.items():
        print(f"{estado}: {percentual:.2f}%")

    rotulos = percentuais_estado.keys()
    tamanhos = percentuais_estado.values()

    fig, ax = plt.subplots()
    ax.pie(tamanhos, labels=rotulos, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title("Distribuição de Faturamento por Estado")

    plt.show()
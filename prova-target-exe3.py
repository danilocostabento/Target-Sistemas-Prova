# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def analyze_revenue(data_file):
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{data_file}' not found.")
        return

    daily_revenue = [item['valor'] for item in data if item['valor'] > 0]


    if not daily_revenue:
        print("Error: No valid revenue data found in the file.")
        return
    
    min_revenue = min(daily_revenue)
    max_revenue = max(daily_revenue)
    average_revenue = sum(daily_revenue) / len(daily_revenue)
    
    days_above_average = sum(1 for revenue in daily_revenue if revenue > average_revenue)

    print(f"Menor valor de faturamento: {min_revenue}")
    print(f"Maior valor de faturamento: {max_revenue}")
    print(f"Média de faturamento mensal: {average_revenue}")
    print(f"Número de dias com faturamento acima da média: {days_above_average}")

analyze_revenue('/content/dados.json')
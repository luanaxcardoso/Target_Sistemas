faturametos_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento = sum(faturametos_estados.values())

percentual_estados = {estado: (faturamento / total_faturamento) * 100 for estado, faturamento in faturametos_estados.items()}

print(percentual_estados)

print("O percentual de representação que cada estado teve dentro do valor total mensal da distribuidora foi:")

for estado, percentual in percentual_estados.items():
    
    print(f"{estado}: {percentual:.2f}%")
    
    
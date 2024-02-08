frase_principal = "Eu Luana, quero fazer parte do time da Target Sistemas!"

frase_invertida = ""

for i in range(len(frase_principal) - 1, -1, -1):
    frase_invertida += frase_principal[i]

print("A frase original é: " + frase_principal + ".")    
print("A frase invertida é: " + frase_invertida + ".")

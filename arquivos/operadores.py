n1 = int(input("Informe um valor inteiro: "))
n2= int(input("Informe outro valor inteiro: "))

# Adição | Subtração | Multiplicação | Divisão

print("Resultado da Adição: " + str( n1 + n2))
print("Resultado da Subtração: " + str( n1 - n2))
print("Resultado da Multiplicação: " + str( n1 * n2))
print("Resultado da Divisão %.2f"  % ( n1 / n2))

# %.2f para arrumar as casas decimais e o % depois para dizer onde o arredondamento é empregado.
# quando quiser fazer com mais valores: % (n1,n2)

#Outra opção:

print(f"Resultado da divisão: {(n1/n2):.3f}")
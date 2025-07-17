print("=== Comparar dois números ==")
# Ler dois números da tela
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
# Comparar os dois números
if(a == b):
    print("Números iguais!")
else:
    print("Números diferentes!")
# Mostrar o número maior
if(a > b):
    print("O maior é ",a)
else:
    print("O maior é",b)
# Mostrar o número menor
if(a < b):
    print("O menor é ",a)
else:
    print("O menor é",b)
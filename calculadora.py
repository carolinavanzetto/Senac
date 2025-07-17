# calculadora.py
 
def main():
    print("=== Calculadora Simples ===")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
 
        print("\nOperações disponíveis:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
 
        opcao = input("Escolha a operação (1/2/3/4): ")
 
        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado da soma: {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado da subtração: {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado da multiplicação: {resultado}")
        elif opcao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da divisão: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Erro: Entrada inválida. Digite números válidos.")
 
if __name__ == "__main__":
    main()
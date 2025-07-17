# padaria.py
 
def main():
    print("=== Sistema de Pedido da Padaria ===")
    cliente = input("Nome do cliente: ")
    produto = input("Nome do produto: ")
 
    try:
        preco = float(input("Preço do produto (R$): "))
        quantidade = int(input("Quantidade: "))
 
        total = preco * quantidade
 
        print("\n=== Dados do Pedido ===")
        print(f"Cliente: {cliente}")
        print(f"Produto: {produto}")
        print(f"Preço unitário: R$ {preco:.2f}")
        print(f"Quantidade: {quantidade}")
        print(f"Total a pagar: R$ {total:.2f}")
 
    except ValueError:
        print("Erro: Entrada inválida. Digite valores numéricos corretamente.")
 
if __name__ == "__main__":
    main()
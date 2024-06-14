from Restaurante4 import Restaurante, ClienteBanco

def main():
    restaurante1 = Restaurante("Restaurante Sabores da Praça")
    restaurante2 = Restaurante("Bistrô da Esquina")
    restaurante3 = Restaurante("Cantina da Mianami")

    restaurante1.adicionar_item_cardapio("Salgadinho Doritos", 5.50)
    restaurante1.adicionar_item_cardapio("Refrigerante", 4.00)
    restaurante2.adicionar_item_cardapio("Conjunto Alimentar Básico", 12.99)
    restaurante3.adicionar_item_cardapio("Coxinha", 3.50)
    restaurante3.adicionar_item_cardapio("Pastel", 5.00)

    Restaurante.listar_restaurantes(restaurante1, restaurante2, restaurante3)

    # Exemplo de uso do cardápio:
    restaurante1.mostrar_cardapio()

    # Exemplo de avaliações
    cliente1 = ClienteBanco("Catarina Lisama", 28, "Designer", "Rua Avenida Franciolo Cascal, 152", "99469-0348")
    cliente2 = ClienteBanco("Carlos Silva", 34, "Engenheiro", "Rua das Flores, 123", "98765-4321")
    cliente3 = ClienteBanco("Ana Paula", 33, "Professor", "Rua Celtinho Almugueiro, 149", "9953-0418")

    restaurante1.adicionar_avaliacao(cliente1, 5, "Excelente comida e atendimento!")
    restaurante1.adicionar_avaliacao(cliente2, 4, "Bom serviço, mas a comida poderia ser melhor.")
    restaurante1.adicionar_avaliacao(cliente3, 3, "Ambiente agradável, mas comida mediana.")

    restaurante1.mostrar_avaliacoes()

if __name__ == "__main__":
    main()

# 1) Primeira parte sendo adicionado o carriiito em classe
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = Carro("camaro", "Preto", 2024)

# 2} Esta classe tá puxando o Restaurante !!!(Adicionando sksksk)
class Restaurante:
    def __init__(self, nome, categoria, ativo, capacidade, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.localizacao = localizacao

meu_restaurante = Restaurante("Restaurante Burlenimsk", "Portuguesa ", True, 50, "Rua Meita de Lorimo")

# 3] Estamos entrando em Modificação do restarzinhoo. (Modificando o Restaurante)
class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=50, localizacao=""):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.localizacao = localizacao
        self.clientes = []
novo_restaurante = Restaurante("Restaurante Japonês", "Japonesa")

# 4) Agora bora lá pro__str__agação pra ir se Restaurar (Adicionando __str__ para a classe Restaurante)
class Restaurante:
    def __init__(self, nome, categoria, ativo=False, capacidade=50, localizacao=""):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.localizacao = localizacao
    
    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}"

restaurante_exemplo = Restaurante("Restaurante Arabes", "Arabe")
print(restaurante_exemplo)


# 5) Entrando Gentaiada (Classe Cliente)

class Cliente:

   class Cliente:

    def __init__(self, nome, idade, genero, endereco):

        self.nome = nome

        self.idade = idade

        self.genero = genero

        self.endereco = endereco



cliente1 = Cliente("Fabio Santiago Maycom", 30, "Masculino", "Rua Almiranda Machado , 763")
print(cliente1.nome, cliente1.idade, cliente1.genero, cliente1.endereco)

cliente2 = Cliente("Elizangela Cristina Macobasso", 25, "Feminino", "Rua Barbélia Margarida, 256")
print(cliente2.nome, cliente2.idade, cliente2.genero, cliente2.endereco)

cliente3 = Cliente("Soares Holiandra Dafonço ", 24, "Masculino", "Rua Carlão Brianlo, 219")
print(cliente3.nome, cliente3.idade, cliente3.genero, cliente3.endereco)

cliente4 = Cliente("Gabriel Kreitom Remiditi ", 29, "Masculino", "Rua PR-723, 199")
print(cliente4.nome, cliente4.idade, cliente4.genero, cliente4.endereco)

cliente5 = Cliente("Miriã Lezumo Pétula", 27, "Feminino", "Apartamento Gahanima Bloco C, 7")
print(cliente5.nome, cliente5.idade, cliente5.genero, cliente5.endereco)

cliente6 = Cliente("Roberta Tatiana Santos", 22, "Feminino", "Rua Télho Francisco Camargo, 219")
print(cliente6.nome, cliente6.idade, cliente6.genero, cliente6.endereco)
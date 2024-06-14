# 1) Criando a Classe de Pessoa
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"Pessoa: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao == "Médico":
            return f"Olá Bem Vindo Dr. {self.nome}"
        elif self.profissao == "Professor":
            return f"Olá Bem Vindo Prof. {self.nome}"
        else:
            return f"Olá Bem Vindo {self.nome}, como vai?"

# 2) Criando uma Classezinha da ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo
        self.ativo = False

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self._saldo}"

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("Não Aceito: Por favor, coloque um número positivo.")

# 3) Criando uma Classe para o ClienteBanco
class ClienteBanco(Pessoa):
    def __init__(self, nome, idade, profissao, endereco, telefone):
        super().__init__(nome, idade, profissao)
        self.endereco = endereco
        self.telefone = telefone

    @classmethod
    def criar_conta(cls, nome, saldo):
        return ContaBancaria(nome, saldo)

# Criando as avaliações dos clientes pro restaurante (avaliação do restaurante)
class Avaliacao:
    def __init__(self, cliente, nota, comentario=""):
        self._validar_nota(nota)
        self.cliente = cliente
        self.nota = nota
        self.comentario = comentario

    def _validar_nota(self, nota):
        if not (1 <= nota <= 5):
            raise ValueError("A nota deve ser um número inteiro entre 1 e 5.")

    def __str__(self):
        return f"Avaliação de {self.cliente.nome}: {self.nota}/5 estrelas - {self.comentario}"

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        self._validar_nota(valor)
        self._nota = valor

# Criando a classe Restaurante
class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.cardapio = []
        self.avaliacoes = []

    def adicionar_item_cardapio(self, item, preco):
        self.cardapio.append((item, preco))

    def mostrar_cardapio(self):
        if not self.cardapio:
            print(f"O cardápio do restaurante {self.nome} está vazio.")
        else:
            print(f"\nCardápio do {self.nome}:")
            for item, preco in self.cardapio:
                print(f"- {item}: R${preco:.2f}")

    def adicionar_avaliacao(self, cliente, nota, comentario=""):
        avaliacao = Avaliacao(cliente, nota, comentario)
        self.avaliacoes.append(avaliacao)

    def mostrar_avaliacoes(self):
        if not self.avaliacoes:
            print(f"O restaurante {self.nome} ainda não tem avaliações.")
        else:
            print(f"\nAvaliações do {self.nome}:")
            for avaliacao in self.avaliacoes:
                print(avaliacao)

    @staticmethod
    def listar_restaurantes(*restaurantes):
        print("\nLista de Restaurantes:")
        for restaurante in restaurantes:
            print(f"- {restaurante.nome}")

# Pessoas fazendo aniversario
pessoa = Pessoa("Roberto Kenlirck Tarto", 32, "Programador")
print(pessoa)
print(pessoa.saudacao)# 1) Criando a Classe de Pessoa
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"Pessoa: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao == "Médico":
            return f"Olá Bem Vindo Dr. {self.nome}"
        elif self.profissao == "Professor":
            return f"Olá Bem Vindo Prof. {self.nome}"
        else:
            return f"Olá Bem Vindo {self.nome}, como vai?"

# 2) Criando uma Classezinha da ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo
        self.ativo = False

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self._saldo}"

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("Não Aceito: Por favor, coloque um número positivo.")

# 3) Criando uma Classe para o ClienteBanco
class ClienteBanco(Pessoa):
    def __init__(self, nome, idade, profissao, endereco, telefone):
        super().__init__(nome, idade, profissao)
        self.endereco = endereco
        self.telefone = telefone

    @classmethod
    def criar_conta(cls, nome, saldo):
        return ContaBancaria(nome, saldo)

# Criando as avaliações dos clentes pro restaurante( avaliação do restaurante )
class Avaliacao:
    def __init__(self, cliente, nota, comentario=""):
        self._validar_nota(nota)
        self.cliente = cliente
        self.nota = nota
        self.comentario = comentario

    def _validar_nota(self, nota):
        if not (1 <= nota <= 5):
            raise ValueError("A nota deve ser um número inteiro entre 1 e 5.")

    def __str__(self):
        return f"Avaliação de {self.cliente.nome}: {self.nota}/5 estrelas - {self.comentario}"

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        self._validar_nota(valor)
        self._nota = valor

# Criando a classe Restaurante
class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.cardapio = []
        self.avaliacoes = []

    def adicionar_item_cardapio(self, item, preco):
        self.cardapio.append((item, preco))

    def mostrar_cardapio(self):
        if not self.cardapio:
            print(f"O cardápio do restaurante {self.nome} está vazio.")
        else:
            print(f"\nCardápio do {self.nome}:")
            for item, preco in self.cardapio:
                print(f"- {item}: R${preco:.2f}")

    def adicionar_avaliacao(self, cliente, nota, comentario=""):
        avaliacao = Avaliacao(cliente, nota, comentario)
        self.avaliacoes.append(avaliacao)

    def mostrar_avaliacoes(self):
        if not self.avaliacoes:
            print(f"O restaurante {self.nome} ainda não tem avaliações.")
        else:
            print(f"\nAvaliações do {self.nome}:")
            for avaliacao in self.avaliacoes:
                print(avaliacao)

    @staticmethod
    def listar_restaurantes(*restaurantes):
        print("\nLista de Restaurantes:")
        for restaurante in restaurantes:
            print(f"- {restaurante.nome}")


# Pessoas fazendo aniversario
pessoa = Pessoa("Roberto Kenlirck Tarto", 32, "Programador")
print(pessoa)
print(pessoa.saudacao)
pessoa.aniversario()
print(pessoa)

# ContaBancaria dos clientes
conta1 = ContaBancaria("Elisabete Alzélia Clara", 1644)
conta2 = ContaBancaria("Lorenzo Malbec", 1510)
conta3 = ContaBancaria("Maicom Leandro", 2190)
conta4 = ContaBancaria("Evelin Franciéle", 1364)
print(conta1)
print(conta2)
print(conta3)
print(conta4)

ContaBancaria.ativar_conta(conta1)
print("Conta ativa:", conta1.ativo)

# Criando os Cliente de Banco (ClienteBanco)
cliente1 = ClienteBanco("Catarina Lisama", 28, "Designer", "Rua Avenida Franciolo Cascal, 152", "99469-0348")
cliente2 = ClienteBanco("Móta Moreira", 32, "Médico", "Rua Liério Consck, 566", "9977-0626")
cliente3 = ClienteBanco("Ana", 33, "Professor", "Rua Celtinho Almugueiro, 149", "9953-0418")

print(cliente1.nome, cliente1.idade, cliente1.profissao)
print(cliente2.nome, cliente2.idade, cliente2.profissao)
print(cliente3.nome, cliente3.idade, cliente3.profissao)

# Criar conta para cliente (conta_cliente)
conta_cliente = ClienteBanco.criar_conta(cliente1.nome, 1040)
print(conta_cliente)

# Produtos do Restaurante
restaurante1 = Restaurante("Restaurante Sabores da Praça")
restaurante1.adicionar_item_cardapio1("Salgadinho Doritos", 7.50)
restaurante1.adicionar_item_cardapio2("Refrigerante Coca Cola", 4.50)
restaurante1.adicionar_item_cardapio3("Refrigerante Fanta", 3.50)
restaurante1.adicionar_item_cardapio4("Coxinha", 4.00)
restaurante1.adicionar_item_cardapio5("Pastel com queijo e presunto", 4.50)
restaurante1.adicionar_item_cardapio6("Salgados encomendado tamanho médio", 19.99)
restaurante1.adicionar_item_cardapio7("Refrigerante Tampico", 3.00)
print(restaurante1.adicionar_item_cardapio1)
print(restaurante1.adicionar_item_cardapio2)
print(restaurante1.adicionar_item_cardapio3)
print(restaurante1.adicionar_item_cardapio4)
print(restaurante1.adicionar_item_cardapio5)
print(restaurante1.adicionar_item_cardapio6)
print(restaurante1.adicionar_item_cardapio7)

# Adicionando avaliações
restaurante1.adicionar_avaliacao(cliente1, 4, "Comida boa e atendimento rápido!")
restaurante1.adicionar_avaliacao(cliente2, 5, "A comida é exelente e o atendimento é perfeito! ")
restaurante1.adicionar_avaliacao(cliente3, 3, "Poderia melhorar a variedade do cardápio.")

# Mostrando as avaliações
restaurante1.mostrar_avaliacoes()

pessoa.aniversario()
print(pessoa)

# ContaBancaria dos clientes
conta1 = ContaBancaria("Elisabete Alzélia Clara", 1644)
conta2 = ContaBancaria("Lorenzo Malbec", 1510)
conta3 = ContaBancaria("Maicom Leandro", 2190)
conta4 = ContaBancaria("Evelin Franciéle", 1364)
print(conta1)
print(conta2)
print(conta3)
print(conta4)

ContaBancaria.ativar_conta(conta1)
print("Conta ativa:", conta1.ativo)

# Criando os Cliente de Banco (ClienteBanco)
cliente1 = ClienteBanco("Catarina Lisama", 28, "Designer", "Rua Avenida Franciolo Cascal, 152", "99469-0348")
cliente2 = ClienteBanco("Móta Moreira", 32, "Médico", "Rua Liério Consck, 566", "9977-0626")
cliente3 = ClienteBanco("Ana", 33, "Professor", "Rua Celtinho Almugueiro, 149", "9953-0418")

print(cliente1.nome, cliente1.idade, cliente1.profissao)
print(cliente2.nome, cliente2.idade, cliente2.profissao)
print(cliente3.nome, cliente3.idade, cliente3.profissao)

# Criar conta para cliente (conta_cliente)
conta_cliente = ClienteBanco.criar_conta(cliente1.nome, 1040)
print(conta_cliente)

# Produtos do Restaurante
restaurante1 = Restaurante("Restaurante Sabores da Praça")
restaurante1.adicionar_item_cardapio("Salgadinho Doritos", 7.50)
restaurante1.adicionar_item_cardapio("Refrigerante Coca Cola", 4.50)
restaurante1.adicionar_item_cardapio("Refrigerante Fanta", 3.50)
restaurante1.adicionar_item_cardapio("Coxinha", 4.00)
restaurante1.adicionar_item_cardapio("Pastel com queijo e presunto", 4.50)
restaurante1.adicionar_item_cardapio("Salgados encomendado tamanho médio", 19.99)
restaurante1.adicionar_item_cardapio("Refrigerante Tampico", 3.00)

# Mostrando o cardápio
restaurante1.mostrar_cardapio()

# Adicionando avaliações
restaurante1.adicionar_avaliacao(cliente1, 4, "Comida boa e atendimento rápido!")
restaurante1.adicionar_avaliacao(cliente2, 5, "A comida é excelente e o atendimento é perfeito!")
restaurante1.adicionar_avaliacao(cliente3, 3, "Poderia melhorar a variedade do cardápio.")

# Mostrando as avaliações
restaurante1.mostrar_avaliacoes()

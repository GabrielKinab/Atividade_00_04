class Avaliacao:
    def __init__(self, cliente, nota, comentario=""):
        self._validar_nota(nota)  # Validação da nota no construtor
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

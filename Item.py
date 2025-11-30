class Item:
    def _init_(self, nome, tipo, efeito, peso):
        self.nome = nome
        self.tipo = tipo
        self.efeito = efeito
        self.peso = peso

    def _str_(self):
        return f"{self.nome} ({self.tipo}, efeito: {self.efeito}, peso: {self.peso})"


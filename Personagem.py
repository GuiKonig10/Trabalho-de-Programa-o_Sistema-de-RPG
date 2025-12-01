from Item import Item
class Personagem:
    def _init_(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
        self.hp_max = 100 + nivel * 10
        self.hp = self.hp_max
        self.capacidade = 50
        self.inventario = []
        self.classe = "Personagem"
        
    def peso_total(self):
        return sum(item.peso for item in self.inventario)

    def adicionar_item(self, item):
        if self.peso_total() + item.peso <= self.capacidade:
            self.inventario.append(item)
            print(f"{item.nome} adicionado ao inventário de {self.nome}.")
        else:
            print("Inventário cheio!")

    def remover_item(self, nome_item):
        for item in self.inventario:
            if item.nome.lower() == nome_item.lower():
                self.inventario.remove(item)
                print(f"{item.nome} removido do inventário de {self.nome}.")
                return
        print("Item não encontrado.")

    def exibir_inventario(self):
        print(f"\nInventário de {self.nome} {self.classe} (Peso {self.peso_total()}/{self.capacidade}):")

        if not self.inventario:
            print("Inventário vazio.")
        else:
            for item in self.inventario:
                print(f"- {item}")

    def usar_pocao(self):
        for item in self.inventario:
            if item.tipo == "poção":
                self.hp += item.efeito
                if self.hp > self.hp_max:
                    self.hp = self.hp_max
                self.inventario.remove(item)
                print(f"{self.nome} usou {item.nome} e recuperou {item.efeito} HP! (HP atual: {self.hp})")
                return
        print(f"{self.nome} não tem poções!")

class Guerreiro(Personagem):
    def _init_(self, nome, nivel):
        super()._init_(nome, nivel)
        self.classe = "Guerreiro"


class Mago(Personagem):
    def _init_(self, nome, nivel):
        super()._init_(nome, nivel)
        self.classe = "Mago"


class Arqueiro(Personagem):
    def _init_(self, nome, nivel):
        super()._init_(nome, nivel)
        self.classe = "Arqueiro"




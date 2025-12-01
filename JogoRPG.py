from Personagem import Guerreiro, Mago, Arqueiro
from Item import Item
from Combate import Combate

class JogoRPG:
    def _init_(self):
        self.personagens = []

    def menu(self):
        while True:
            print("\n===== MENU RPG =====")
            print("1. Criar personagem")
            print("2. Adicionar item")
            print("3. Remover item")
            print("4. Exibir inventário")
            print("5. Usar poção")
            print("6. Simular combate")
            print("0. Sair")
            opcao = input("Escolha: ")

            if opcao == "1":
                self.criar_personagem()

            elif opcao == "2":
                self.adicionar_item()

            elif opcao == "3":
                self.remover_item()

            elif opcao == "4":
                self.exibir_inventario()

            elif opcao == "5":
                self.usar_pocao()

            elif opcao == "6":
                self.simular_combate()

            elif opcao == "0":
                print("Saindo do jogo...")
                break

            else:
                print("Opção inválida!")

    def escolher_personagem(self):
        if not self.personagens:
            print("Nenhum personagem cadastrado!")
            return None

        for i, p in enumerate(self.personagens):
            print(f"{i+1}. {p.nome} ({p.classe}) - HP: {p.hp}")

        idx = int(input("Escolha o personagem: ")) - 1
        return self.personagens[idx]

    def criar_personagem(self):
        nome = input("Nome: ")
        nivel = int(input("Nível: "))
        
        print("\nEscolha a classe:")
        print("1. Guerreiro")
        print("2. Mago")
        print("3. Arqueiro")
        escolha = input("Classe: ")

        if escolha == "1":
            p = Guerreiro(nome, nivel)
        elif escolha == "2":
            p = Mago(nome, nivel)
        elif escolha == "3":
            p = Arqueiro(nome, nivel)
        else:
            print("Classe inválida!")
            return

        self.personagens.append(p)
        print(f"{p.classe} {nome} criado!")

    def adicionar_item(self):
        p = self.escolher_personagem()
        if not p:
            return

        nome = input("Nome do item: ")
        tipo = input("Tipo (arma, poção, equipamento): ")
        efeito = int(input("Efeito: "))
        peso = int(input("Peso: "))

        item = Item(nome, tipo, efeito, peso)
        p.adicionar_item(item)

    def remover_item(self):
        p = self.escolher_personagem()
        if not p:
            return

        nome = input("Nome do item para remover: ")
        p.remover_item(nome)

    def exibir_inventario(self):
        for p in self.personagens:
            p.exibir_inventario()

    def usar_pocao(self):
        p = self.escolher_personagem()
        if p:
            p.usar_pocao()

    def simular_combate(self):
        if len(self.personagens) < 2:
            print("São necessários pelo menos 2 personagens!")
            return

        print("Escolha o primeiro lutador:")
        p1 = self.escolher_personagem()

        print("Escolha o segundo lutador:")
        p2 = self.escolher_personagem()

        if p1 and p2 and p1 != p2:
            Combate.lutar(p1, p2)
        else:
            print("Combate inválido!")

jogo = JogoRPG()
jogo.menu()

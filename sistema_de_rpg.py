import random

def criar_personagem(nome, classe, nivel):
    hp = 100 + nivel * 2
    capacidade = 50
    inventario = []
    return [nome, classe, nivel, hp, capacidade, inventario]

def criar_item(nome, tipo, efeito, peso):
    return [nome, tipo, efeito, peso]

def peso_inventario(personagem):
    return sum(item[3] for item in personagem[5])

def adicionar_item(personagem, item):
    if peso_inventario(personagem) + item[3] <= personagem[4]:
        personagem[5].append(item)
        print(f"{item[0]} adicionado ao inventário de {personagem[0]}.")
    else:
        print("Inventário cheio!")

def remover_item(personagem, nome_item):
    for item in personagem[5]:
        if item[0].lower() == nome_item.lower():
            personagem[5].remove(item)
            print(f"{item[0]} removido do inventário de {personagem[0]}.")
            return
    print("Item não encontrado.")

def exibir_inventario(personagem):
    print(f"\nInventário de {personagem[0]} (Peso {peso_inventario(personagem)}/{personagem[4]}):")
    if not personagem[5]:
        print("Inventário vazio.")
    else:
        for item in personagem[5]:
            print(f"- {item[0]} ({item[1]}, efeito: {item[2]}, peso: {item[3]})")

def usar_pocao(personagem):
    for item in personagem[5]:
        if item[1] == "poção":
            personagem[3] += item[2]
            if personagem[3] > 100 + personagem[2] * 10:
                personagem[3] = 100 + personagem[2] * 10
            personagem[5].remove(item)
            print(f"{personagem[0]} usou {item[0]} e recuperou {item[2]} HP! (HP atual: {personagem[3]})")
            return
    print(f"{personagem[0]} não tem poções!")


def combate(p1, p2):
    print(f"\nCombate entre {p1[0]} e {p2[0]} começou!")
    while p1[3] > 0 and p2[3] > 0:
        atacante, defensor = (p1, p2) if random.choice([True, False]) else (p2, p1)
        dano = random.randint(5, 15) + atacante[2]
        defensor[3] -= dano
        print(f"{atacante[0]} atacou {defensor[0]} causando {dano} de dano! (HP {defensor[0]}: {defensor[3]})")
        if defensor[3] <= 0:
            print(f"\n{atacante[0]} venceu o combate!")
            return

def menu():
    personagens = []

    while True:
        print("\n===== MENU RPG =====")
        print(". Criar personagem")
        print("2. Adicionar item ao inventário")
        print("3. Remover item do inventário")
        print("4. Exibir inventário")
        print("5. Usar poção")
        print("6. Simular combate")
        print("0. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do personagem: ")
            classe = input("Classe: ")
            nivel = int(input("Nível: "))
            p = criar_personagem(nome, classe, nivel)
            personagens.append(p)
            print(f"Personagem {nome} criado!")

        elif opcao == "2":
            if not personagens:
                print("Nenhum personagem cadastrado!")
                continue
            for i, p in enumerate(personagens):
                print(f"{i+1}. {p[0]}")
            idx = int(input("Escolha o personagem: ")) - 1

            nome_item = input("Nome do item: ")
            tipo = input("Tipo (arma, poção, equipamento): ")
            efeito = int(input("Efeito (ex: dano ou cura): "))
            peso = int(input("Peso: "))
            item = criar_item(nome_item, tipo, efeito, peso)
            adicionar_item(personagens[idx], item)

        elif opcao == "3":
            if not personagens:
                print("Nenhum personagem cadastrado!")
                continue
            for i, p in enumerate(personagens):
                print(f"{i+1}. {p[0]}")
            idx = int(input("Escolha o personagem: ")) - 1
            nome_item = input("Nome do item para remover: ")
            remover_item(personagens[idx], nome_item)

        elif opcao == "4":
            if not personagens:
                print("Nenhum personagem cadastrado!")
                continue
            for p in personagens:
                exibir_inventario(p)

        elif opcao == "5":
            if not personagens:
                print("Nenhum personagem cadastrado!")
                continue
            for i, p in enumerate(personagens):
                print(f"{i+1}. {p[0]} (HP: {p[3]})")
            idx = int(input("Escolha o personagem: ")) - 1
            usar_pocao(personagens[idx])

        elif opcao == "6":
            if len(personagens) < 2:
                print("São necessários pelo menos 2 personagens!")
                continue
            for i, p in enumerate(personagens):
                print(f"{i+1}. {p[0]} (HP: {p[3]})")
            p1 = int(input("Escolha o primeiro: ")) - 1
            p2 = int(input("Escolha o segundo: ")) - 1
            combate(personagens[p1], personagens[p2])

        elif opcao == "0":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida!")

menu()


        
    





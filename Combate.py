class Combate:
    @staticmethod
    def lutar(p1, p2):
        print(f"\nCombate entre {p1.nome} ({p1.classe}) e {p2.nome} ({p2.classe}) começou!")

        while p1.hp > 0 and p2.hp > 0:
            atacante, defensor = (p1, p2) if random.choice([True, False]) else (p2, p1)
            
            dano = random.randint(5, 15) + atacante.nivel
            defensor.hp -= dano

            print(f"{atacante.nome} atacou {defensor.nome} causando {dano} de dano! (HP {defensor.nome}: {defensor.hp})")

            if defensor.hp <= 0:
                print(f"\n{atacante.nome} venceu o combate!")
                return


import random

class TreinoFutebolCompleto:
    def __init__(self, nivel, dificuldades, dias_disponiveis):
        self.nivel = nivel.lower()
        self.dificuldades = dificuldades
        self.dias_disponiveis = dias_disponiveis

        self.treinos_por_dificuldade = {
            "finalizacao": [
                "Finalizações rápidas após passe curto",
                "Chutes de média distância com ambas as pernas",
                "Cabeceio ofensivo após cruzamentos"
            ],
            "controle de bola": [
                "Controle orientado após passes",
                "Recepção em espaço reduzido",
                "Condução curta com mudança de direção"
            ],
            "passe": [
                "Troca de passes rápidos em campo reduzido",
                "Passe longo de precisão",
                "Triangulações rápidas"
            ],
            "drible": [
                "Drible em cones curtos",
                "1x1 contra marcador",
                "Dribles em velocidade"
            ],
            "visao de jogo": [
                "Jogos reduzidos 5x5 focando tomada de decisão",
                "Passe sob pressão",
                "Posse de bola com restrição de toques"
            ]
        }

        self.treinos_complementares = {
            "resistencia": [
                "Corrida intervalada 4x6min forte",
                "Circuito físico com bola (20min)",
                "Corrida contínua 45min"
            ],
            "agilidade": [
                "Cones em zigue-zague com bola",
                "Saltos laterais rápidos",
                "Ladder drill (escada de agilidade)"
            ],
            "velocidade": [
                "Sprints de 20-40m",
                "Arranques explosivos com bola",
                "Corrida intervalada curta"
            ],
            "forca": [
                "Treino funcional com peso corporal",
                "Agachamento + arranque explosivo",
                "Pliometria com saltos"
            ],
            "tatica": [
                "Jogo reduzido 7x7 com objetivo específico",
                "Exercício de posicionamento defensivo",
                "Treino de movimentação ofensiva"
            ],
            "regenerativo": [
                "Corrida leve 20min",
                "Alongamento guiado 15min",
                "Exercícios de mobilidade"
            ]
        }

    def gerar_treino(self):
        cronograma = {}
        for i, dia in enumerate(self.dias_disponiveis):
            treino_dia = []
            if i < len(self.dificuldades):
                dificuldade = self.dificuldades[i]
                treino_especifico = random.choice(self.treinos_por_dificuldade.get(dificuldade, ["Exercício geral"]))
                treino_dia.append(f"Foco em {dificuldade.capitalize()} → {treino_especifico}")

            chaves_complementares = list(self.treinos_complementares.keys())
            tema = chaves_complementares[i % len(chaves_complementares)]
            treino_complementar = random.choice(self.treinos_complementares[tema])
            treino_dia.append(f"Complementar ({tema.capitalize()}) → {treino_complementar}")

            cronograma[dia] = treino_dia

        return cronograma


# ---------------------- MENU INTERATIVO ----------------------
def montar_treino_futebol():
    print("=== PLANO PERSONALIZADO DE TREINO DE FUTEBOL ===\n")

    # Nível
    niveis = ["Iniciante", "Intermediário", "Avançado"]
    print("Escolha seu nível:")
    for i, n in enumerate(niveis, 1):
        print(f"{i} - {n}")
    nivel_escolha = int(input("Digite o número: ")) - 1
    nivel = niveis[nivel_escolha]

    # Dificuldades
    dificuldades_disponiveis = ["Finalizacao", "Controle de bola", "Passe", "Drible", "Visao de jogo"]
    print("\nEscolha suas dificuldades (digite os números separados por vírgula):")
    for i, d in enumerate(dificuldades_disponiveis, 1):
        print(f"{i} - {d}")
    escolhas = input("Digite aqui: ").split(",")
    dificuldades = [dificuldades_disponiveis[int(x)-1].lower() for x in escolhas]

    # Dias de treino
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    print("\nEscolha os dias de treino (digite os números separados por vírgula):")
    for i, d in enumerate(dias_semana, 1):
        print(f"{i} - {d}")
    escolhas_dias = input("Digite aqui: ").split(",")
    dias_disponiveis = [dias_semana[int(x)-1] for x in escolhas_dias]

    # Gera treino
    futebol = TreinoFutebolCompleto(nivel, dificuldades, dias_disponiveis)
    cronograma = futebol.gerar_treino()

    print("\n=== SEU CRONOGRAMA PERSONALIZADO ===")
    for dia, treinos in cronograma.items():
        print(f"\n📅 {dia}:")
        for treino in treinos:
            print(f"   - {treino}")


# ---------------------- EXECUTAR ----------------------
if __name__ == "__main__":
    montar_treino_futebol()

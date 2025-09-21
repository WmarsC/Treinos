import random

class TreinoBasquete:
    def __init__(self, dificuldades, dias_disponiveis):
        self.dificuldades = dificuldades  # lista de dificuldades escolhidas pelo usuário
        self.dias_disponiveis = dias_disponiveis  # lista de dias da semana

        # Base de exercícios por tipo
        self.exercicios = {
            "finalizacao": [
                "Lay-up com mão dominante",
                "Lay-up com mão não dominante",
                "Bandeja em movimento",
                "Finalização sobre pressão"
            ],
            "drible": [
                "Drible entre cones",
                "Drible rápido em linha reta",
                "Drible de proteção de bola",
                "Drible em velocidade com mudança de direção"
            ],
            "passe": [
                "Passe peito rápido",
                "Passe picado",
                "Passe com movimentação",
                "Passe em pressão"
            ],
            "defesa": [
                "Deslocamento lateral defensivo",
                "Fechar espaço no bloqueio",
                "Marcação individual",
                "Defesa em dupla"
            ],
            "arremesso": [
                "Arremesso parado",
                "Arremesso em movimento",
                "Arremesso sob pressão",
                "Free throws"
            ],
            "resistencia": [
                "Corrida contínua 15-20min",
                "Circuito cardio com bola",
                "Shuttle run",
                "Corrida intervalada"
            ],
            "agilidade": [
                "Cone drills",
                "Ladder drills",
                "Mudança de direção rápida",
                "Sprints curtos alternados"
            ],
            "velocidade": [
                "Sprints de 20-30m",
                "Sprints em subida",
                "Reações rápidas ao apito",
                "Tiros explosivos com bola"
            ],
            "forca": [
                "Agachamento com salto",
                "Pliometria",
                "Flexões explosivas",
                "Treino com elástico de resistência"
            ],
            "impulsao": [
                "Saltos verticais com apoio de parede",
                "Saltos com caixa pliométrica",
                "Saltos com agachamento profundo",
                "Burpees explosivos",
                "Sprints com salto final"
            ],
            "tatica": [
                "Treino de pick and roll",
                "Jogadas ensaiadas",
                "Posicionamento ofensivo/defensivo",
                "Leitura de jogo"
            ],
            "regenerativo": [
                "Alongamento dinâmico",
                "Corrida leve 10-15min",
                "Yoga para atletas",
                "Recuperação ativa com bola leve"
            ]
        }

    def gerar_treino_dia(self):
        treino_dia = []

        # Para cada dificuldade escolhida, seleciona um exercício aleatório
        for dif in self.dificuldades:
            treino_dia.append(f"✅ {dif.capitalize()}: {random.choice(self.exercicios[dif])}")

        # Adiciona exercícios complementares para atributos físicos, incluindo impulsão
        complementares = ["resistencia", "agilidade", "velocidade", "forca", "impulsao", "tatica", "regenerativo"]
        for comp in complementares:
            treino_dia.append(f"💪 {comp.capitalize()}: {random.choice(self.exercicios[comp])}")

        return treino_dia

    def gerar_cronograma(self):
        cronograma = {}
        dias = self.dias_disponiveis[:len(self.dias_disponiveis)]
        for dia in dias:
            cronograma[dia] = self.gerar_treino_dia()
        return cronograma


# ---------------------- INTERATIVO ----------------------
def montar_treino_basquete():
    print("=== PLANO DE TREINO PARA BASQUETE ===\n")

    # Seleção das dificuldades
    opcoes = ["finalizacao", "drible", "passe", "defesa", "arremesso"]
    print("Escolha suas dificuldades (digite os números separados por vírgula):")
    for i, opc in enumerate(opcoes, 1):
        print(f"  {i}. {opc.capitalize()}")
    escolhas = input("Opções: ")
    dificuldades = [opcoes[int(x.strip()) - 1] for x in escolhas.split(",") if x.strip().isdigit()]

    # Seleção dos dias da semana
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    print("\nEscolha os dias que você pode treinar (digite os números separados por vírgula):")
    for i, dia in enumerate(dias_semana, 1):
        print(f"  {i}. {dia}")
    dias_input = input("Opções: ")
    dias_disponiveis = [dias_semana[int(x.strip()) - 1] for x in dias_input.split(",") if x.strip().isdigit()]

    # Gerar treino
    basquete = TreinoBasquete(dificuldades, dias_disponiveis)
    cronograma = basquete.gerar_cronograma()

    # Exibir cronograma
    print("\n=== SEU CRONOGRAMA DE BASQUETE ===")
    for dia, treino in cronograma.items():
        print(f"\n📅 {dia}:")
        for linha in treino:
            print(f"  {linha}")


# ---------------------- EXECUTAR ----------------------
if __name__ == "__main__":
    montar_treino_basquete()

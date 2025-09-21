import random

class TreinoVolei:
    def __init__(self, dificuldades, dias_disponiveis):
        self.dificuldades = dificuldades
        self.dias_disponiveis = dias_disponiveis

        # Base de exercícios por tipo
        self.exercicios = {
            "saque": [
                "Saque flutuante",
                "Saque viagem",
                "Saque por cima em movimento",
                "Saque de precisão visando áreas"
            ],
            "bloqueio": [
                "Bloqueio individual",
                "Bloqueio duplo",
                "Deslocamento lateral no bloqueio",
                "Bloqueio em salto rápido"
            ],
            "ataque": [
                "Ataque de meio",
                "Ataque de ponta",
                "Ataque em cruzamento",
                "Ataque em situação de contra-ataque"
            ],
            "defesa": [
                "Recepção de saque",
                "Defesa em mergulho",
                "Deslocamento rápido para defesa",
                "Defesa com reflexos rápidos"
            ],
            "passe": [
                "Passe de toque",
                "Passe de manchete",
                "Passe em movimento",
                "Passe sob pressão"
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
                "Sprints em deslocamento lateral",
                "Reações rápidas ao apito",
                "Tiros explosivos"
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
                "Burpees explosivos"
            ],
            "tatica": [
                "Treino de posicionamento em quadra",
                "Jogadas ensaiadas",
                "Cobertura de espaços",
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

        # Exercícios para dificuldades escolhidas
        for dif in self.dificuldades:
            treino_dia.append(f"✅ {dif.capitalize()}: {random.choice(self.exercicios[dif])}")

        # Exercícios complementares
        complementares = ["resistencia", "agilidade", "velocidade", "forca", "impulsao", "tatica", "regenerativo"]
        for comp in complementares:
            treino_dia.append(f"💪 {comp.capitalize()}: {random.choice(self.exercicios[comp])}")

        return treino_dia

    def gerar_cronograma(self):
        cronograma = {}
        for dia in self.dias_disponiveis:
            cronograma[dia] = self.gerar_treino_dia()
        return cronograma


# ---------------------- INTERATIVO ----------------------
def montar_treino_volei():
    print("=== PLANO DE TREINO PARA VÔLEI ===\n")

    # Seleção das dificuldades
    opcoes = ["saque", "bloqueio", "ataque", "defesa", "passe"]
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
    volei = TreinoVolei(dificuldades, dias_disponiveis)
    cronograma = volei.gerar_cronograma()

    # Exibir cronograma
    print("\n=== SEU CRONOGRAMA DE VÔLEI ===")
    for dia, treino in cronograma.items():
        print(f"\n📅 {dia}:")
        for linha in treino:
            print(f"  {linha}")


# ---------------------- EXECUTAR ----------------------
if __name__ == "__main__":
    montar_treino_volei()

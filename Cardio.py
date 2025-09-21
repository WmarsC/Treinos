import random

class CardioProgram:
    def __init__(self, nivel, intensidade, dias_disponiveis, duracao=30, modalidade="misto"):
        self.nivel = nivel.lower()
        self.intensidade = intensidade.lower()
        self.dias_disponiveis = dias_disponiveis
        self.duracao = duracao
        self.modalidade = modalidade.lower()

        self.exercicios = {
            "esteira": ["Caminhada Leve", "Corrida Moderada", "Sprints"],
            "bike": ["Pedalada Leve", "Pedalada Moderada", "Sprints Bike"],
            "eliptico": ["Elíptico Leve", "Elíptico Moderado", "HIIT Elíptico"],
            "livre": ["Polichinelo", "Burpee", "Pular Corda", "Corrida no Lugar"],
            "misto": ["HIIT", "Circuito Cardio", "Treino Funcional"]
        }

        self.parametros_nivel = {
            "iniciante": 2,
            "intermediário": 3,
            "avançado": 4
        }

    def escolher_exercicios(self):
        if self.modalidade in self.exercicios:
            return random.sample(self.exercicios[self.modalidade], k=min(2, len(self.exercicios[self.modalidade])))
        else:
            return random.sample(self.exercicios["misto"], k=2)

    def gerar_treino_dia(self):
        intervalo = self.parametros_nivel.get(self.nivel, 2)
        aquecimento = "Caminhada Leve 5 min" if self.modalidade == "esteira" else "Aquecimento Articular 5 min"
        principais = self.escolher_exercicios()
        desaquecimento = "Alongamento e Respiração 5 min"

        treino = [f"👉 Aquecimento: {aquecimento}"]
        tempo_por_exercicio = max(5, (self.duracao - 10) // len(principais))
        for ex in principais:
            treino.append(f"👉 {ex}: {tempo_por_exercicio} min (intervalo {intervalo} min entre blocos)")
        treino.append(f"👉 Desaquecimento: {desaquecimento}")

        return treino

    def gerar_cronograma(self):
        cronograma = {}
        for dia in self.dias_disponiveis:
            cronograma[dia] = {
                "nivel": self.nivel,
                "intensidade": self.intensidade,
                "duracao": self.duracao,
                "treino": self.gerar_treino_dia()
            }
        return cronograma


# ---------------------- INTERATIVO COM OPÇÕES ----------------------
def montar_cardio_interativo():
    print("=== MONTAR PLANO DE CARDIO ===\n")

    # Nível
    niveis = ["iniciante", "intermediário", "avançado"]
    print("Escolha seu nível:")
    for i, nv in enumerate(niveis, 1):
        print(f"  {i}. {nv.capitalize()}")
    nivel = niveis[int(input("Digite o número do nível: ")) - 1]

    # Intensidade
    intensidades = ["leve", "moderado", "alto"]
    print("\nEscolha a intensidade do treino:")
    for i, it in enumerate(intensidades, 1):
        print(f"  {i}. {it.capitalize()}")
    intensidade = intensidades[int(input("Digite o número da intensidade: ")) - 1]

    # Dias da semana
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    print("\nEscolha os dias que você pode treinar (digite os números separados por vírgula):")
    for i, dia in enumerate(dias_semana, 1):
        print(f"  {i}. {dia}")
    dias_input = input("Opções: ")
    dias_disponiveis = [dias_semana[int(x.strip()) - 1] for x in dias_input.split(",") if x.strip().isdigit()]

    # Modalidade
    modalidades = ["esteira", "bike", "elíptico", "livre", "misto"]
    print("\nEscolha a modalidade:")
    for i, mod in enumerate(modalidades, 1):
        print(f"  {i}. {mod.capitalize()}")
    modalidade = modalidades[int(input("Digite o número da modalidade: ")) - 1]

    # Duração
    duracao = int(input("\nEscolha a duração do treino em minutos (ex: 30): "))

    # Gerar treino
    cardio = CardioProgram(nivel, intensidade, dias_disponiveis, duracao, modalidade)
    cronograma = cardio.gerar_cronograma()

    # Exibir cronograma
    print("\n=== SEU CRONOGRAMA DE CARDIO ===")
    for dia, dados in cronograma.items():
        print(f"\n📅 {dia} - Intensidade: {dados['intensidade'].capitalize()} | Duração: {dados['duracao']} min")
        for linha in dados["treino"]:
            print(linha)


# ---------------------- EXECUTAR ----------------------
if __name__ == "__main__":
    montar_cardio_interativo()

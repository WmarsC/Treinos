import random

class TreinoReabilitacao:
    def __init__(self, parte_corpo, local):
        self.parte_corpo = parte_corpo.lower()
        self.local = local.lower()

        # Base de exercícios por parte do corpo e local
        self.exercicios = {
            "ombro": {
                "casa": ["Elevação lateral com garrafa d'água", "Rotação externa com elástico", "Alongamento de ombro"],
                "livre": ["Flexão de braço modificada", "Remada com halteres leves", "Elevação frontal com halteres"],
                "equipamentos": ["Peck Deck leve", "Rotação externa na polia", "Desenvolvimento máquina leve"]
            },
            "joelho": {
                "casa": ["Agachamento parcial", "Extensão de perna sentado", "Elevação de perna reta"],
                "livre": ["Leg press leve", "Agachamento com halteres leves", "Avanço controlado"],
                "equipamentos": ["Cadeira extensora leve", "Cadeira flexora leve", "Leg curl máquina"]
            },
            "tornozelo": {
                "casa": ["Elevação de panturrilha", "Flexão plantar com elástico", "Movimentos circulares do tornozelo"],
                "livre": ["Saltos pequenos controlados", "Caminhada na ponta dos pés", "Pliometria leve"],
                "equipamentos": ["Máquina de panturrilha", "Stepper leve", "Equilíbrio na bosu"]
            },
            "quadril": {
                "casa": ["Elevação de quadril", "Abdução de quadril com elástico", "Alongamento de flexores"],
                "livre": ["Agachamento sumô leve", "Passada lateral", "Stiff leve com halteres"],
                "equipamentos": ["Leg press amplo", "Cadeira abdutora", "Cadeira adutora"]
            },
            "costas": {
                "casa": ["Prancha frontal", "Superman", "Alongamento de gato-vaca"],
                "livre": ["Remada unilateral com halteres", "Hiperextensão no banco", "Ponte de glúteo"],
                "equipamentos": ["Remada baixa máquina leve", "Pulldown frente leve", "Extensão lombar máquina"]
            },
            "punho": {
                "casa": ["Flexão e extensão com peso leve", "Rotação de punho com elástico", "Apertos de bola de borracha"],
                "livre": ["Rosca inversa leve", "Flexão de punho com halteres", "Alongamento de punho"],
                "equipamentos": ["Extensor de punho máquina", "Flexor de punho máquina"]
            },
            "cotovelo": {
                "casa": ["Flexão e extensão com elástico", "Tríceps kickback leve", "Alongamento de cotovelo"],
                "livre": ["Rosca direta leve", "Tríceps francês halteres leves"],
                "equipamentos": ["Rosca Scott máquina leve", "Tríceps polia baixa leve"]
            },
            "pescoço": {
                "casa": ["Inclinação lateral", "Flexão e extensão controlada", "Rotação lenta do pescoço"],
                "livre": ["Alongamento cervical com resistência leve", "Isometria do pescoço"],
                "equipamentos": ["Máquina de extensão cervical leve", "Máquina de flexão cervical leve"]
            },
            "peito": {
                "casa": ["Flexão de braço contra a parede", "Flexão de joelhos", "Alongamento peitoral"],
                "livre": ["Supino com halteres leves", "Flexão inclinada", "Crucifixo leve"],
                "equipamentos": ["Supino máquina leve", "Peck Deck leve", "Crossover leve"]
            },
            "perna": {
                "casa": ["Agachamento parcial", "Afundo sem peso", "Elevação de panturrilha"],
                "livre": ["Agachamento com halteres leves", "Passada lateral", "Stiff leve"],
                "equipamentos": ["Leg press leve", "Cadeira extensora/flexora leve", "Glúteo polia leve"]
            }
        }

        self.complementares = {
            "fortalecimento": ["Prancha 30s", "Isometria", "Alongamento dinâmico leve", "Exercícios de resistência elástica"],
            "mobilidade": ["Rotação de articulação", "Alongamento suave", "Movimentos de amplitude controlada"],
            "estabilidade": ["Equilíbrio em uma perna", "Exercícios proprioceptivos", "Bosu ou almofada instável"],
            "regenerativo": ["Respiração profunda", "Caminhada leve", "Alongamento passivo"]
        }

    def gerar_treino(self):
        treino = []

        # Exercícios principais para a parte do corpo e local escolhidos
        if self.parte_corpo in self.exercicios and self.local in self.exercicios[self.parte_corpo]:
            principais = random.sample(self.exercicios[self.parte_corpo][self.local], k=min(3, len(self.exercicios[self.parte_corpo][self.local])))
            treino.extend([f"✅ {ex}" for ex in principais])
        else:
            treino.append("⚠️ Exercícios gerais de reabilitação: use movimentos suaves e alongamentos controlados")

        # Adiciona exercícios complementares
        for tipo, lista in self.complementares.items():
            treino.append(f"💪 {tipo.capitalize()}: {random.choice(lista)}")

        return treino


# ---------------------- INTERATIVO ----------------------
def montar_treino_reabilitacao():
    print("=== PLANO DE TREINO DE REABILITAÇÃO / FORTALECIMENTO ===\n")

    # Seleção da parte do corpo
    partes = ["ombro", "joelho", "tornozelo", "quadril", "costas", "punho", "cotovelo", "pescoço", "peito", "perna"]
    print("Escolha a parte do corpo que precisa recuperar:")
    for i, parte in enumerate(partes, 1):
        print(f"  {i}. {parte.capitalize()}")
    escolha_parte = int(input("Digite o número: "))
    parte_corpo = partes[escolha_parte - 1]

    # Seleção do local
    locais = ["casa", "livre", "equipamentos"]
    print("\nEscolha onde você quer fazer o treino:")
    for i, local in enumerate(locais, 1):
        print(f"  {i}. {local.capitalize()}")
    escolha_local = int(input("Digite o número: "))
    local = locais[escolha_local - 1]

    # Gerar treino
    rehab = TreinoReabilitacao(parte_corpo, local)
    treino = rehab.gerar_treino()

    # Exibir treino
    print(f"\n=== SEU TREINO DE REABILITAÇÃO PARA {parte_corpo.capitalize()} ({local.capitalize()}) ===")
    for linha in treino:
        print(f"  {linha}")


# ---------------------- EXECUTAR ----------------------
if __name__ == "__main__":
    montar_treino_reabilitacao()

import random

class TreinoCorrida:
    def __init__(self, nivel, dias_disponiveis):
        self.nivel = nivel.lower()
        self.dias_disponiveis = dias_disponiveis

        # Base de treinos por tipo (expandida)
        self.tipos_treino = {
            "longao": [
                "Corrida longa em ritmo confortável",
                "Corrida progressiva de longa distância",
                "Corrida em trilha (trail run leve)",
                "Fartlek longo (alternar ritmo a cada 5 min)",
                "Corrida contínua 60-90min"
            ],
            "tiros": [
                "8x400m forte com pausa de 2min",
                "10x200m forte com pausa de 1min",
                "5x1000m em ritmo forte",
                "6x800m ritmo de prova, pausa 90s",
                "15x100m tiros curtos explosivos",
                "3x2000m ritmo forte, pausa 3min"
            ],
            "regenerativo": [
                "Corrida leve 30-40min",
                "Trote regenerativo 20-30min",
                "Corrida em ritmo de conversa",
                "Caminhada rápida 40min",
                "Yoga + corrida leve 20min"
            ],
            "educativos": [
                "Skipping alto",
                "Skipping baixo",
                "Drills de corrida (A/B/C)",
                "Deslocamento lateral",
                "Corrida em subida leve",
                "Pliometria leve",
                "Saltitos coordenados"
            ],
            "forca": [
                "Treino de subidas curtas explosivas",
                "Corrida com resistência elástica",
                "Sprints em rampa",
                "Treino de pliometria avançada",
                "Tiros em escada (subir degraus correndo)"
            ]
        }

        # Estrutura de distribuição de treinos por semana
        self.plano_por_nivel = {
            "iniciante": ["longao", "regenerativo", "educativos"],
            "intermediário": ["longao", "tiros", "regenerativo", "educativos"],
            "avançado": ["longao", "tiros", "tiros", "regenerativo", "forca", "educativos"]
        }

    def gerar_treino_dia(self, tipo):
        return random.choice(self.tipos_treino[tipo])

    def gerar_cronograma(self):
        cronograma = {}
        plano = self.plano_por_nivel.get(self.nivel, self.plano_por_nivel["iniciante"])

        # Ajusta para quantidade de dias disponíveis
        dias = self.dias_disponiveis[:len(plano)]

        for i, dia in enumerate(dias):
            tipo_treino = plano[i]
            cronograma[dia] = {
                "tipo": tipo_treino.capitalize(),
                "descricao": self.gerar_treino_dia(tipo_treino)
            }

        return cronograma


# ---------------------- INTERATIVO COM OPÇÕES ----------------------
def montar_treino_corrida():
    print("=== PLANO DE TREINO PARA CORRIDA ===\n")

    # Escolha do nível
    niveis = ["iniciante", "intermediário", "avançado"]
    print("Escolha seu nível:")
    for i, nv in enumerate(niveis, 1):
        print(f"  {i}. {nv.capitalize()}")
    nivel = niveis[int(input("Digite o número do nível: ")) - 1]

    # Escolha dos dias da semana
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    print("\nEscolha os dias que você pode treinar (digite os números separados por vírgula):")
    for i, dia in enumerate(dias_semana, 1):
        print(f"  {i}. {dia}")
    dias_input = input("Opções: ")
    dias_disponiveis = [dias_semana[int(x.strip()) - 1] for x in dias_input.split(",") if x.strip().isdigit()]

    # Montar treino
    corrida = TreinoCorrida(nivel, dias_disponiveis)
    cronograma = corrida.gerar_cronograma()

    # Exibir resultado
    print("\n=== SEU CRONOGRAMA DE CORRIDA ===")
    for dia, treino in cronograma.items():
        print(f"📅 {dia}: {treino['tipo']} - {treino['descricao']}")


# ---------------------- EXECUTAR ----------------------
if __name__ == "__main__":
    montar_treino_corrida()

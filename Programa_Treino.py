import random

# Banco de exercícios categorizados por objetivo e equipamento
exercicios = {
    "hipertrofia": {
        "A - Peito/Tríceps/Ombro": {
            "Peito": {
                "máquinas": ["Supino Máquina", "Peck Deck"],
                "livres": ["Supino Reto Barra", "Supino Inclinado Halteres", "Crucifixo"],
                "misto": ["Supino Inclinado Barra", "Crossover", "Supino Halteres"]
            },
            "Tríceps": {
                "máquinas": ["Tríceps Corda na Polia", "Tríceps Testa Máquina"],
                "livres": ["Tríceps Testa Barra", "Mergulho"],
                "misto": ["Tríceps Francês Halteres", "Tríceps Kickback"]
            },
            "Ombro": {
                "máquinas": ["Desenvolvimento Máquina", "Elevação Lateral Máquina"],
                "livres": ["Desenvolvimento Militar Barra", "Elevação Lateral Halteres", "Arnold Press"],
                "misto": ["Desenvolvimento Halteres", "Remada Alta Barra"]
            }
        },
        "B - Costas/Bíceps": {
            "Costas": {
                "máquinas": ["Puxada na Frente", "Remada Baixa Máquina"],
                "livres": ["Barra Fixa", "Remada Curvada Barra", "Levantamento Terra"],
                "misto": ["Pulldown Polia", "Remada Unilateral Halteres"]
            },
            "Bíceps": {
                "máquinas": ["Rosca Scott Máquina", "Rosca Direta Máquina"],
                "livres": ["Rosca Direta Barra", "Rosca Alternada Halteres"],
                "misto": ["Rosca Martelo", "Rosca Concentrada"]
            }
        },
        "C - Pernas/Glúteo/Core": {
            "Pernas": {
                "máquinas": ["Leg Press", "Cadeira Extensora", "Cadeira Flexora"],
                "livres": ["Agachamento Livre", "Afundo", "Passada"],
                "misto": ["Agachamento Smith", "Stiff Halteres"]
            },
            "Glúteo": {
                "máquinas": ["Cadeira Abdutora", "Glúteo Máquina"],
                "livres": ["Hip Thrust", "Avanço"],
                "misto": ["Glúteo Polia", "Elevação Pélvica Barra"]
            },
            "Core": {
                "máquinas": ["Abdominal Máquina"],
                "livres": ["Prancha", "Abdominal Supra", "Abdominal Bicicleta"],
                "misto": ["Prancha com Peso", "Abdominal com Halteres"]
            }
        }
    },
    "emagrecimento": {
        "A - Cardio + FullBody": {
            "Cardio": {
                "máquinas": ["Bicicleta Ergométrica", "Esteira Caminhada"],
                "livres": ["Corrida Livre", "Burpee"],
                "misto": ["HIIT Esteira", "Corda Naval"]
            },
            "FullBody": {
                "máquinas": ["Leg Press", "Supino Máquina"],
                "livres": ["Flexão", "Agachamento Livre"],
                "misto": ["Kettlebell Swing", "Thruster"]
            }
        },
        "B - Resistência Muscular": {
            "Pernas": {
                "máquinas": ["Cadeira Extensora", "Cadeira Flexora"],
                "livres": ["Afundo", "Passada"],
                "misto": ["Agachamento Smith", "Stiff Halteres"]
            },
            "Braços": {
                "máquinas": ["Rosca Direta Máquina"],
                "livres": ["Flexão de Braço", "Rosca Alternada Halteres"],
                "misto": ["Rosca Martelo", "Flexão com Carga"]
            },
            "Core": {
                "máquinas": ["Abdominal Máquina"],
                "livres": ["Prancha", "Abdominal Infra"],
                "misto": ["Prancha com Peso", "Abdominal com Halteres"]
            }
        },
        "C - Misto": {
            "Cardio": {
                "máquinas": ["Elíptico", "Bicicleta Ergométrica"],
                "livres": ["Corrida Livre", "Polichinelo"],
                "misto": ["HIIT", "Pular Corda"]
            },
            "FullBody": {
                "máquinas": ["Supino Máquina", "Leg Press"],
                "livres": ["Mountain Climber", "Agachamento com Salto"],
                "misto": ["Clean and Press", "Kettlebell Swing"]
            }
        }
    },
    "resistência": {
        "A - Circuito Força": {
            "Circuito": {
                "máquinas": ["Supino Máquina", "Remada Máquina", "Leg Press"],
                "livres": ["Burpee", "Flexão", "Agachamento Livre", "Prancha"],
                "misto": ["Kettlebell Swing", "Barra Fixa", "Thruster"]
            }
        },
        "B - Circuito Cardio": {
            "Circuito": {
                "máquinas": ["Bicicleta Ergométrica", "Elíptico", "Esteira"],
                "livres": ["Polichinelo", "Corrida no Lugar", "Mountain Climber"],
                "misto": ["HIIT", "Pular Corda", "Corda Naval"]
            }
        },
        "C - Circuito Misto": {
            "Circuito": {
                "máquinas": ["Remada Máquina", "Leg Press"],
                "livres": ["Afundo", "Abdominal", "Agachamento Livre"],
                "misto": ["Barra Fixa", "Kettlebell Swing", "Clean and Jerk"]
            }
        }
    }
}

# Séries e repetições adaptados por objetivo e nível
parametros = {
    "hipertrofia": {
        "iniciante": {"series": "3", "reps": "10-12"},
        "intermediário": {"series": "3-4", "reps": "8-12"},
        "avançado": {"series": "4-5", "reps": "6-10"}
    },
    "emagrecimento": {
        "iniciante": {"series": "2", "reps": "15-20"},
        "intermediário": {"series": "3", "reps": "12-15"},
        "avançado": {"series": "3-4", "reps": "15-20 + cardio extra"}
    },
    "resistência": {
        "iniciante": {"series": "Circuito 1-2x", "reps": "30s cada"},
        "intermediário": {"series": "Circuito 2-3x", "reps": "40s cada"},
        "avançado": {"series": "Circuito 3-4x", "reps": "60s cada"}
    }
}

def gerar_treino(objetivo, nivel, dias_semana, equipamento):
    plano = list(exercicios[objetivo].items())
    qtd_treinos = len(plano)

    # Montagem do cronograma
    if dias_semana >= qtd_treinos:
        cronograma = [plano[i % qtd_treinos] for i in range(dias_semana)]
    elif dias_semana == 2:
        cronograma = [plano[0], plano[1]]
    elif dias_semana == 1:
        cronograma = [("Full Body", {"Corpo Todo": {
            "máquinas": ["Leg Press", "Supino Máquina", "Remada Máquina"],
            "livres": ["Agachamento Livre", "Flexão", "Prancha"],
            "misto": ["Agachamento Smith", "Kettlebell Swing", "Pulldown Polia"]
        }})]
    else:
        cronograma = plano[:dias_semana]

    # Exibe o treino
    print(f"\n🏋️ Plano de Treino para {objetivo.capitalize()} - {nivel.capitalize()} ({equipamento})\n")
    for i, (dia, grupos) in enumerate(cronograma, start=1):
        print(f"\n📅 Dia {i} - {dia}:")
        for grupo, opcoes in grupos.items():
            if equipamento not in opcoes:
                continue
            escolhidos = random.sample(opcoes[equipamento], k=min(2, len(opcoes[equipamento])) )
            print(f"   {grupo}: {', '.join(escolhidos)}")
        s = parametros[objetivo][nivel]["series"]
        r = parametros[objetivo][nivel]["reps"]
        print(f"   ➝ Séries: {s} | Reps: {r}")

# Programa principal
print("🏋️ Bem-vindo ao Gerador de Treino de Academia!\n")

# Escolha do objetivo
objetivos = list(exercicios.keys())
print("Escolha seu objetivo:")
for i, obj in enumerate(objetivos, 1):
    print(f"  {i}. {obj.capitalize()}")
objetivo = objetivos[int(input("Digite o número do objetivo: ")) - 1]

# Escolha do nível
niveis = list(parametros[objetivo].keys())
print("\nEscolha seu nível:")
for i, nv in enumerate(niveis, 1):
    print(f"  {i}. {nv.capitalize()}")
nivel = niveis[int(input("Digite o número do nível: ")) - 1]

# Dias por semana
dias = int(input("\nQuantos dias por semana você pode treinar? "))

# Escolha do equipamento
opcoes_eq = ["máquinas", "livres", "misto"]
print("\nEscolha seu tipo de treino:")
for i, eq in enumerate(opcoes_eq, 1):
    print(f"  {i}. {eq.capitalize()}")
equipamento = opcoes_eq[int(input("Digite o número da opção: ")) - 1]

# Gerar plano
gerar_treino(objetivo, nivel, dias, equipamento)

from robot_modelo import Robot
from robot_vista import mostrar_estado, mostrar_combate, mostrar_reporte, mostrar_habilidad
import random
import time

robots = [
    Robot("AlphaX", 100),
    Robot("OmegaZ", 100),
    Robot("CyberQ", 100)
]

# Asignar habilidades distintas
robots[0].habilidad = "doble_ataque"
robots[1].habilidad = "escudo_total"
robots[2].habilidad = "regeneracion"

print("🚀 Estado Inicial:")
for robot in robots:
    mostrar_estado(robot)

rondas = 0
print("\n🤖 ¡Inicia el torneo todos contra todos!")

while sum(r.estado == "Activo" for r in robots) > 1:
    rondas += 1
    print(f"\n🔁 Ronda {rondas}")
    vivos = [r for r in robots if r.estado == "Activo"]
    atacante = random.choice(vivos)
    defensor = random.choice([r for r in vivos if r != atacante])

    habilidad = atacante.usar_habilidad()
    if habilidad:
        mostrar_habilidad(atacante, habilidad)

    multiplicador = 2 if habilidad == "doble_ataque" else 1
    danio = random.randint(10, 30) * multiplicador

    mostrar_combate(atacante, defensor, danio)
    defensor.recibir_danio(danio)
    atacante.danio_infligido += danio
    mostrar_estado(defensor)

    time.sleep(1)

mostrar_reporte(robots, rondas)


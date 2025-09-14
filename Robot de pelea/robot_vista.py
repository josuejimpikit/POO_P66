def mostrar_estado(robot):
    print(f"🤖 {robot.nombre} | Energía: {robot.energia:.1f} | Estado: {robot.estado}")

def mostrar_combate(atacante, defensor, danio):
    print(f"⚔️ {atacante.nombre} ataca a {defensor.nombre} con {danio} de daño!")

def mostrar_habilidad(robot, habilidad):
    if habilidad == "doble_ataque":
        print(f"💥 {robot.nombre} activó su habilidad especial: DOBLE ATAQUE!")
    elif habilidad == "escudo_total":
        print(f"🛡️ {robot.nombre} activó su ESCUDO TOTAL por esta ronda!")
    elif habilidad == "regeneracion":
        print(f"❤️ {robot.nombre} usó REGENERACIÓN y recuperó energía!")

def mostrar_reporte(robots, rondas):
    print("\n📊 Reporte de Batalla:")
    print(f"Rondas jugadas: {rondas}")
    for robot in robots:
        print(f"{robot.nombre} -> Estado: {robot.estado}, Energía restante: {robot.energia:.1f}, Daño recibido: {robot.danio_recibido:.1f}, Daño infligido: {robot.danio_infligido:.1f}")
    vivos = [r for r in robots if r.estado != "Destruido"]
    if vivos:
        print(f"🏆 Ganador(es): {', '.join(r.nombre for r in vivos)}")
    else:
        print("❌ No hubo ganadores, todos fueron destruidos.")

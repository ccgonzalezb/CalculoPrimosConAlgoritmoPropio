def criba_tercio_optima(limite, progreso_callback=None):
    conjunto_inicial = set(range(2, limite + 1))
    primos_encontrados = []
    tope_cribado = (limite**0.5) + 1
    total = limite - 1  # para el progreso

    while conjunto_inicial:
        primo = min(conjunto_inicial)
        primos_encontrados.append(primo)

        if primo > tope_cribado:
            primos_encontrados.extend(sorted(conjunto_inicial - {primo}))
            break

        subconjunto = set(range(primo * 2, limite + 1, primo))
        conjunto_inicial -= subconjunto
        conjunto_inicial.discard(primo)

        # Enviar progreso si se provee callback
        if progreso_callback:
            progreso = int((total - len(conjunto_inicial)) / total * 100)
            progreso_callback(progreso)

    return primos_encontrados

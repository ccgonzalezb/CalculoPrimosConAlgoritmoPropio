import time

def criba_eratostenes(limite):
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False
    for i in range(2, int(limite**0.5) + 1):
        if primos[i]:
            for j in range(i*i, limite + 1, i):
                primos[j] = False
    return [i for i, es_primo in enumerate(primos) if es_primo]

def criba_tercio_optima(limite):
    conjunto_inicial = set(range(2, limite + 1))
    primos_encontrados = []
    tope_cribado = (limite**0.5) + 1

    while conjunto_inicial:
        primo = min(conjunto_inicial)
        primos_encontrados.append(primo)

        if primo > tope_cribado:
            primos_encontrados.extend(sorted(conjunto_inicial - {primo}))
            break

        subconjunto = set(range(primo * 2, limite + 1, primo))
        conjunto_inicial -= subconjunto
        conjunto_inicial.discard(primo)

    return primos_encontrados

# Comparación de rendimiento
limite = 1000000

inicio = time.time()
primos_eratostenes = criba_eratostenes(limite)
tiempo_eratostenes = time.time() - inicio
print(f"Tiempo Eratóstenes: {tiempo_eratostenes:.4f} segundos")

inicio = time.time()
primos_tercio = criba_tercio_optima(limite)
tiempo_tercio = time.time() - inicio
print(f"Tiempo Tercio Optimizada: {tiempo_tercio:.4f} segundos")


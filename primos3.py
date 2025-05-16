import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def criba_tercio_optima(limite):
    conjunto_inicial = set(range(2, limite + 1))
    primos_encontrados = []
    tope_cribado = (limite**0.5) + 1
    multiples = []

    # Para la animación, iremos guardando el estado de los conjuntos
    animacion_data = []

    while conjunto_inicial:
        primo = min(conjunto_inicial)
        primos_encontrados.append(primo)

        # Añadir estado actual a la animación
        animacion_data.append((list(conjunto_inicial), multiples))

        # Si el primo supera el tope, los restantes son todos primos
        if primo > tope_cribado:
            animacion_data.append((sorted(conjunto_inicial), multiples))  # Agregar el estado final
            break

        # Generar y eliminar múltiplos
        subconjunto = set(range(primo * 2, limite + 1, primo))
        multiples.append(subconjunto)  # Guardar los múltiplos
        conjunto_inicial -= subconjunto
        conjunto_inicial.discard(primo)

    return primos_encontrados, animacion_data

# Función para crear la animación
def animar_criba(limite):
    primos, animacion_data = criba_tercio_optima(limite)

    # Inicializar la figura y el eje
    fig, ax = plt.subplots()
    ax.set_xlim(0, limite)
    ax.set_ylim(0, 1)
    ax.set_yticks([])  # Sin etiquetas en el eje Y
    ax.set_xticks(range(0, limite + 1, 10))

    # Inicializar los elementos de la animación
    puntos, = ax.plot([], [], 'bo', label='Posibles primos', markersize=4)
    descartados, = ax.plot([], [], 'ro', label='Números descartados', markersize=4)
    primos_linea, = ax.plot([], [], 'go', label='Primos encontrados', markersize=6)
    multiples_linea, = ax.plot([], [], 'rx', label='Múltiplos descartados', markersize=5)

    def init():
        puntos.set_data([], [])
        descartados.set_data([], [])
        primos_linea.set_data([], [])
        multiples_linea.set_data([], [])
        return puntos, descartados, primos_linea, multiples_linea

    # Función de actualización de la animación
    def update(frame):
        conjunto_inicial, multiples = animacion_data[frame]

        # Actualizar los puntos en la gráfica
        puntos.set_data([x for x in conjunto_inicial], [0] * len(conjunto_inicial))
        descartados.set_data([x for x in multiples[-1]], [0] * len(multiples[-1]))
        
        # Mostrar los primos encontrados
        primos_linea.set_data(primos[:frame + 1], [0] * (frame + 1))
        
        # Actualizar los múltiplos descartados
        multiples_linea.set_data([x for sublist in multiples for x in sublist], [0] * len([x for sublist in multiples for x in sublist]))
        
        return puntos, descartados, primos_linea, multiples_linea

    # Crear la animación
    ani = animation.FuncAnimation(fig, update, frames=len(animacion_data), init_func=init, blit=True, interval=1000000)

    plt.legend()
    plt.title(f"Criba de Eratóstenes hasta {limite}")
    plt.show()

# Probar la animación con el límite 100
animar_criba(1000000)

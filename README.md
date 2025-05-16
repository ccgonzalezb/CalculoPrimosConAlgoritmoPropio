# Proyecto: Prueba matemática sobre números primos

Este proyecto en Python tiene como objetivo probar y demostrar el concepto matemático de que:

> "Un número primo es el primer elemento de un subconjunto contenido en los números naturales."

## Descripción

La idea principal es implementar un algoritmo que identifique números primos utilizando un enfoque basado en subconjuntos del conjunto de los números naturales. En particular, el algoritmo encuentra primos como el primer elemento en ciertos subconjuntos generados a partir de los naturales.

Este proyecto incluye:

- Implementación del algoritmo `criba_tercio_optima` para encontrar números primos hasta un límite dado.
- Interfaz gráfica en PyQt5 para facilitar la interacción con el usuario.
- Visualización del progreso y resultados.

## Requisitos

- Python 3.7 o superior
- PyQt5

Para instalar PyQt5, ejecuta:

pip install PyQt5

Uso
1 Ejecuta la aplicación:
    python main.py

2 Ingresa un número límite en la caja de texto.

3 Presiona el botón Calcular Primos.

4 Observa el progreso y los primeros números primos encontrados en pantalla.

Notas
Para no saturar la interfaz, solo se muestran los primeros 1000 números primos.

El cálculo puede tardar más para límites muy grandes.

Autor
Cristian Camilo González Blanco
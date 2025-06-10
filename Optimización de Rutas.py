def dfs_ruta_mas_corta(grafo, inicio, destino, visitados=None, camino_actual=None, distancia_actual=0, mejor_ruta=None, mejor_distancia=float('inf')):
    if visitados is None:
        visitados = set()
    if camino_actual is None:
        camino_actual = []

    # Añadir la ciudad actual al camino y marcarla como visitada
    visitados.add(inicio)
    camino_actual.append(inicio)

    # Si llegamos al destino, verificamos si es la mejor ruta
    if inicio == destino:
        if distancia_actual < mejor_distancia:
            mejor_ruta = camino_actual[:]
            mejor_distancia = distancia_actual
    else:
        # Explorar las ciudades vecinas
        for vecino, distancia in grafo.get(inicio, {}).items():
            if vecino not in visitados:
                mejor_ruta, mejor_distancia = dfs_ruta_mas_corta(
                    grafo, vecino, destino, visitados, camino_actual, 
                    distancia_actual + distancia, mejor_ruta, mejor_distancia
                )

    # Retroceder en la búsqueda
    visitados.remove(inicio)
    camino_actual.pop()

    return mejor_ruta, mejor_distancia


def encontrar_ruta_mas_corta(grafo, entrada):
    # Dividir la entrada en ciudad de inicio y destino
    if len(entrada.split()) != 2:
        return "None"  # Validación básica si la entrada no es válida
    inicio, destino = entrada.split()
    inicio, destino = inicio.upper(), destino.upper()  # Convertir a mayúsculas

    if inicio not in grafo or destino not in grafo:
        return "None"  # Si alguna ciudad no está en el grafo

    camino, _ = dfs_ruta_mas_corta(grafo, inicio, destino)
    return " ".join(camino) if camino else "None"


# Interfaz de usuario para ingresar datos
if __name__ == "__main__":
    grafo = {
        'A': {'B': 5, 'C': 8, 'D': 9},
        'B': {'A': 5, 'E': 15, 'F': 7},
        'C': {'A': 8, 'G': 12, 'H': 10},
        'D': {'A': 9, 'I': 11, 'J': 6},
        'E': {'B': 15, 'K': 9, 'L': 13},
        'F': {'B': 7, 'M': 8, 'N': 6},
        'G': {'C': 12, 'O': 10, 'P': 5},
        'H': {'C': 10, 'Q': 11, 'R': 7},
        'I': {'D': 11, 'S': 14, 'T': 8},
        'J': {'D': 6, 'U': 9, 'V': 12},
        'K': {'E': 9},
        'L': {'E': 13},
        'M': {'F': 8},
        'N': {'F': 6},
        'O': {'G': 10},
        'P': {'G': 5},
        'Q': {'H': 11},
        'R': {'H': 7},
        'S': {'I': 14},
        'T': {'I': 8},
        'U': {'J': 9},
        'V': {'J': 12}
    }

    entrada = input().strip()
    resultado = encontrar_ruta_mas_corta(grafo, entrada)
    print(resultado)
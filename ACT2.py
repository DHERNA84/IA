# Importamos las bibliotecas necesarias
import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo para representar el sistema de transporte
G = nx.Graph()

# Añadimos las estaciones al grafo como nodos
stations = ["EST-1", "EST-2", "EST-3", "EST-4", "EST-5", "EST-6", "EST-7", "EST-8", "EST-9", "EST-10"]
G.add_nodes_from(stations)

# Añadimos rutas al grafo como aristas
routes = [
    ("EST-1", "EST-2"),
    ("EST-2", "EST-3"),
    ("EST-3", "EST-4"),
    ("EST-4", "EST-5"),
    ("EST-1", "EST-5"),  # Ruta adicional
    ("EST-2", "EST-6"),  # Ruta adicional
    ("EST-4", "EST-10"),  # Ruta adicional
    ("EST-6", "EST-9"),  # Ruta adicional
    ("EST-5", "EST-6"),
    ("EST-6", "EST-7"),
    ("EST-7", "EST-8"),
    ("EST-8", "EST-10"),
    # Añade más rutas según sea necesario
]
G.add_edges_from(routes)

# Definimos una función para encontrar la mejor ruta entre dos estaciones
def encontrar_mejor_ruta(G, inicio, fin):
    try:
        return nx.shortest_path(G, inicio, fin)
    except nx.NetworkXNoPath:
        return None

# Función para dibujar el grafo y la ruta
def dibujar_grafo_y_ruta(G, ruta):
    pos = nx.spring_layout(G, seed=42)  # Posición fija para reproducibilidad
    nx.draw(G, pos, with_labels=True)

    if ruta:
        # Dibujamos la ruta en rojo
        ruta_edges = [(ruta[i], ruta[i+1]) for i in range(len(ruta)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=ruta_edges, edge_color='r', width=2)
    else:
        print("No hay ruta disponible entre las estaciones ingresadas.")

    # Mostramos el grafo con la ruta (si existe)
    plt.show()

# Función para interactuar con el usuario y encontrar la ruta
def buscar_ruta_interactiva():
    while True:
        inicio = input("Ingresa la estación de inicio (1-10): ")
        fin = input("Ingresa la estación de destino (1-10): ")

        # Mapeo de entrada a nombres completos de estaciones
        estaciones = {
            "1": "EST-1",
            "2": "EST-2",
            "3": "EST-3",
            "4": "EST-4",
            "5": "EST-5",
            "6": "EST-6",
            "7": "EST-7",
            "8": "EST-8",
            "9": "EST-9",
            "10": "EST-10"
        }

        try:
            inicio = estaciones[inicio]
            fin = estaciones[fin]
            mejor_ruta = encontrar_mejor_ruta(G, inicio, fin)
            print("La mejor ruta es:", mejor_ruta)
            dibujar_grafo_y_ruta(G, mejor_ruta)
        except KeyError:
            print("Estación no válida. Ingresa un número del 1 al 10.")

        continuar = input("¿Deseas buscar otra ruta? (s/n): ")
        if continuar.lower() != 's':
            break

# Iniciamos la búsqueda interactiva
buscar_ruta_interactiva()

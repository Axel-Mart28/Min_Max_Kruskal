import networkx as nx
import matplotlib.pyplot as plt

# --- CLASE AUXILIAR: UNION-FIND ---
# Esta estructura es la forma estandar de detectar ciclos en Kruskal.
# Sirve para saber a qué "familia" (conjunto) pertenece cada nodo.
class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
    
    def find(self, node):
        # Busca el representante (raiz) del conjunto
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])
    
    def union(self, u, v):
        # Une dos conjuntos
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v
            return True # Union exitosa
        return False # Ya estaban unidos (formaria ciclo)

# --- FUNCIÓN DE INGRESO DE DATOS ---
def crear_grafo_usuario():
    G = nx.Graph()
    print("\n--- CONFIGURACIÓN DEL GRAFO ---")
    print("Ingresa las conexiones: Origen Destino Peso")
    print("Ejemplo: A B 5 (o 0 1 5)")
    print("Escribe 'fin' para terminar.\n")

    while True:
        entrada = input(">> Ingresa arista (u v w): ")
        if entrada.lower() == 'fin':
            break
        try:
            datos = entrada.split()
            if len(datos) != 3:
                print("Error: Ingresa 3 valores.")
                continue
            u, v, w = datos[0], datos[1], int(datos[2])
            G.add_edge(u, v, weight=w)
        except ValueError:
            print("Error: El peso debe ser un número entero.")
    return G

# --- ALGORITMO KRUSKAL VISUAL ---
def simulador_kruskal(G, modo='min'):
    # 1. Preparacion Visual
    pos = nx.spring_layout(G, seed=42)
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # 2. Ordenar aristas
    # Si es 'min', ordena ascendente. Si es 'max', descendente (reverse=True)
    reverse_sort = True if modo == 'max' else False
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'], reverse=reverse_sort)
    
    uf = UnionFind(G.nodes())
    mst_edges = []      # Aristas aceptadas (Verde)
    rejected_edges = [] # Aristas rechazadas por ciclo (Rojo punteado)
    
    texto_modo = "MÁXIMO" if modo == 'max' else "MÍNIMO"
    print(f"\n{'='*40}")
    print(f"INICIO KRUSKAL - ÁRBOL DE {texto_modo} COSTE")
    print(f"Aristas ordenadas: {[(u, v, d['weight']) for u, v, d in edges_sorted]}")
    print(f"{'='*40}\n")
    
    step = 1
    total_cost = 0
    
    for u, v, data in edges_sorted:
        weight = data['weight']
        
        # --- DIBUJAR ESTADO BASE ---
        ax.clear()
        ax.set_title(f"Kruskal ({texto_modo}) - Paso {step}\nEvaluando: {u}-{v} ({weight})", fontsize=14)
        
        # Fondo
        nx.draw(G, pos, ax=ax, with_labels=True, node_color='lightgray', 
                edge_color='lightgray', style='dotted', node_size=700)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
        
        # Dibujar aristas ya procesadas
        if mst_edges:
            nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='green', width=3, ax=ax)
        if rejected_edges:
            nx.draw_networkx_edges(G, pos, edgelist=rejected_edges, edge_color='red', style='dashed', alpha=0.5, ax=ax)
            
        # Dibujar arista ACTUAL (En evaluación - Azul)
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], edge_color='blue', width=4, ax=ax)
        
        plt.pause(1.5) # Pausa para ver qué arista se está evaluando
        
        # --- LÓGICA DE KRUSKAL ---
        es_ciclo = False
        if uf.union(u, v):
            # No hay ciclo, se acepta
            print(f"Paso {step}: Arista ({u}-{v}, w={weight}) -> ACEPTADA (Une componentes)")
            mst_edges.append((u, v))
            total_cost += weight
            # Pintar confirmación verde momentánea
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], edge_color='lime', width=5, ax=ax)
        else:
            # Hay ciclo, se rechaza
            print(f"Paso {step}: Arista ({u}-{v}, w={weight}) -> RECHAZADA (Forma ciclo)")
            rejected_edges.append((u, v))
            es_ciclo = True
            # Pintar rechazo rojo momentáneo
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], edge_color='red', width=5, ax=ax)

        plt.pause(1.0)
        step += 1

    # --- RESULTADO FINAL ---
    ax.clear()
    ax.set_title(f"Árbol de {texto_modo} Coste Completado\nCosto Total: {total_cost}", fontsize=16, color='green')
    
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='#90EE90', edge_color='lightgray', style='dotted', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
    # Solo dibujamos el MST final limpio
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='green', width=3)
    
    print(f"\n{'='*40}")
    print(f"FIN. Costo Total: {total_cost}")
    print(f"Aristas finales: {mst_edges}")
    
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    grafo = crear_grafo_usuario()
    if len(grafo.edges) > 0:
        opcion = input("\n¿Qué deseas simular? (min/max): ").lower().strip()
        if opcion in ['min', 'max']:
            simulador_kruskal(grafo, modo=opcion)
        else:
            print("Opción no válida. Se ejecutará Mínimo por defecto.")
            simulador_kruskal(grafo, modo='min')
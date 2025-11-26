<h1> En este repositorio de encuentra un simulador paso a paso del algoritmo de Arbol Maximo y Minimo de Kruskal, en el cuál el usuario ingresa el grafo con los nodos y pesos, y se muestra gráficamente como se va resolviendo paso a paso </h1>
<h2> Ejemplo de ejecución: </h2>


<h3> 
    --- CONFIGURACIÓN DEL GRAFO ---
    <br>
    Ingresa las conexiones: Origen Destino Peso
    <br>
    Ejemplo: A B 5 (o 0 1 5)
    <br>
    Escribe 'fin' para terminar.
    <br>

    >> Ingresa arista (u v w): A B 10
    >> Ingresa arista (u v w): B C 5
    >> Ingresa arista (u v w): A C 20
    >> Ingresa arista (u v w): fin

    ¿Qué deseas simular? (min/max): min

    ========================================
    INICIO KRUSKAL - ÁRBOL DE MÍNIMO COSTE
    Aristas ordenadas: [('B', 'C', 5), ('A', 'B', 10), ('A', 'C', 20)]
    ========================================

    Paso 1: Arista (B-C, w=5) -> ACEPTADA (Une componentes)
    Paso 2: Arista (A-B, w=10) -> ACEPTADA (Une componentes)
    Paso 3: Arista (A-C, w=20) -> RECHAZADA (Forma ciclo)

    ========================================
    FIN. Costo Total: 15
    Aristas finales: [('B', 'C'), ('A', 'B')]
</h3>
<br>
 <p>
  <img src="images/minimo.png" alt="Ejecución de Prim" width="600">
</p>

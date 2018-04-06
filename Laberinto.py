class Nodo ():
    def __init__(self, valor, hijos = []):
        self.valor=valor
        self.hijos=hijos

        
def insertar(arbol,valor):
    if arbol==None:
        return Nodo(valor)
    elif(buscar(arbol ,valor)):
        return arbol
    else:
        arbol.hijos.append(Nodo(valor))
        return arbol

def crearNodo(arbol, valor):
    if arbol ==None:
        return Nodo(valor,[])
    elif  (buscar(arbol,valor)):
        return arbol
    else:
        return Nodo(arbol.valor, validarVecinos(cargarArchivo(),valor,arbol))

    
def validarVecinos (laberinto,posicion, arbol):
    arriba=[posicion[0],posicion[1]-1]
    abajo= [posicion[0],posicion[1]+1]
    derecha= [posicion[0]+1,posicion[1]]
    izquierda= [posicion[0]-1,posicion[1]]
 
    if ("x" in laberinto[posicion[0]][posicion[1]] or "0" in laberinto[posicion[0]][posicion[1]]):
        print(listarArbol(arbol))
        validarVecinos(laberinto,arriba,insertar(arbol , arriba))
        validarVecinos(laberinto,abajo,insertar(arbol , abajo))
        validarVecinos(laberinto,derecha,insertar(arbol , derecha))
        validarVecinos(laberinto,izquierda,insertar(arbol , izquierda))
        if laberinto[posicion[0]-1][posicion[1]]=="0":           
            print("gola1")
            arbol = insertar(arbol,[posicion[0]-1,posicion[1]])
            return validarVecinos(laberinto,[4,4],arbol)
        if laberinto[posicion[0]][posicion[1]-1]=="0":
            print("gola2")
            arbol = insertar(arbol, [[posicion[0]],[posicion[1]-1]])
            return validarVecinos(laberinto,[posicion[0],posicion[1]-1],arbol)
        if laberinto[posicion[0]+1][posicion[1]]=="0":
            print("gola3")
            arbol = insertar(arbol, [[posicion[0]+1],[posicion[1]]])
            return validarVecinos(laberinto,[posicion[0]+1,posicion[1]],arbol)
        if laberinto[posicion[0]][posicion[1]+1]=="0":
            print("gol4a")
            arbol = insertar(arbol, [[posicion[0]],[posicion[1]+1]])
            return validarVecinos(laberinto,[posicion[0],posicion[1]+1],arbol)
    return arbol;

def cargarArchivo():
    laberinto = [list(linea)[:-1] for linea in open ("Laberinto.txt").readlines()]
    return laberinto

def buscar (arbol, valor):
    if arbol==None :
        return False
    if arbol.valor==valor:
        return True
    return buscar_hijos(arbol.hijos, valor)

def buscar_hijos (hijos,valor):
    if hijos==[]:
        return False
    return buscar(hijos[0],valor) or buscar_hijos(hijos[1:],valor)

def buscarX (laberinto):
    for x in range(len(laberinto)):
        for y in range(len(laberinto[x])):
            if "x" in str(laberinto[x][y]) :
                posicion=[x,y]
                
                return posicion

def listarArbol(arbol):
    if(arbol==None):
        return []
    else:
        return [arbol.valor] + listar(arbol.hijos)

def listar(hijos):
    if hijos == []:
        return []
    else:
        return [hijos[0].valor] + listar(hijos[1:])

def buscarX(laberinto):
    for x in range(len(laberinto)):
        for y in range(len(laberinto[x])):
            if "x" in laberinto[x][y] :                
                return [x,y]


#Prueba del programa. Se hace una lectura de archivo .txt que contiene un laberinto
arbol = insertar(None, buscarX(cargarArchivo()))
print(listarArbol(validarVecinos(cargarArchivo(), buscarX(cargarArchivo()), arbol)))
arbol = Nodo(5,[Nodo(10),Nodo(20)])
arbol = Nodo(5, Nodo(10,Nodo(20,None)))
print(listarArbol(arbol))
print (buscar(arbol,20))
arbol = insertar(arbol,  6)
print (buscar(arbol,6))
print(listarArbol(arbol))
arbol = insertar(arbol, 6)
print(listarArbol(arbol))

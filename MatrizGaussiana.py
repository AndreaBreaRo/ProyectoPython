"""
Andrea Brea Rodríguez

Práctica final del módulo de Python. 
     La función process_matrix recibe una matriz de cualquier tamaño y procesa una nueva con los vecinos de cada pixel,
     por cada pixel procesado en la matriz:
        1 - Crea una lista de objetos con las posibles coordenadas vecinas.
        2 - Crea una nueva lista donde filtra los objetos que no son posibles debido a que están fuera del rango de la matriz. 
        3 - Crea una lista con los valores de las coordenadas que son correctas
        4 - Calcula la media de esa lista
        5- La imprime en dicha coordenada 
"""
from functools import reduce

###########################FUNCIÓN PRINCIPAL####################################

def process_matrix(matrix):
    """
    Función que gestiona los posibles errores que puede tener la matriz
    """
    if matrix == []:
        return []
    elif is_numerical_matrix(matrix) == True:
        newMatrix = _process_matrix(matrix)
    else:
        raise ValueError('Only works on numerical matrices') 
    return newMatrix 

##################################################################################

class coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_neighbour_indices(i,j):

    """
    Se instancian los indices de las posibles coordenadas, lo que da un lista de objetos
    """
    list=[]
    list.append(coordenadas(i,j))  #center
    list.append(coordenadas(i+1,j))    #up
    list.append(coordenadas(i-1,j))  #down
    list.append(coordenadas(i,j+1)) #right
    list.append(coordenadas(i,j-1))  #left

    return tuple(list)


def get_size_matrix(matrix):
    """
    Función que devuelve el tamaño de la matriz en filas, columnas y elementos totales de la matriz
    """
    row = len(matrix) 
    col = len(matrix[0])
    return row, col


def filter_neighbourgs(ROW, COL, list):
    """
    Función que crea una tupla con los objetos válidos.   
    """
    list_objects=[]
    for coord in list:
        if(coord.x >= 0 and coord.y >= 0) and (coord.x <ROW and coord.y < COL):
            list_objects.append(coord)
        
    return tuple(list_objects)


def process_element(list, matrix):
    """
    Función recorre la tupla de objetos coordenadas válidos e introduce los valores de la matriz en una lista
    """
    list_values=[]
    for coord_filtered in list:
        list_values.append(matrix[coord_filtered.x][coord_filtered.y])
    
    return list_values

def get_average(list):
    """"
    Recibe uns lista de números y devuelve su promedio 
    """
    return reduce(lambda i, j: i + j, list) / len(list)


def _process_matrix(matrix):
    """
    Función principal que calcula la media de los vecinos y crea una nueva matriz
    """
    #Obtener el tamaño de la matriz por filas y columnas, no tiene porqué ser cuadrada.
    [ROW, COL]=get_size_matrix(matrix)
    # Generar la nueva matriz 
    newMatrix=[]
    for i in range(ROW):
        row=[]
        for j in range(COL):
            list = get_neighbour_indices(i,j)
            list_objects = filter_neighbourgs(ROW, COL, list)
            list_values = process_element(list_objects, matrix)
            average = get_average(list_values)
            row.append(average)
        newMatrix.append(row)  

    return newMatrix

######################## PARTE OPCIONAL##########################

def is_numerical_matrix(matrix):
    """
    Función que comprueba que matrix es una lista de listas, que las sublistas son todas del mismo tamaño
    y el contenido de las sublistas son todo números. Si cumple las tres condiciones devuelve un verdadero. 
    """

    def input_is_list_of_lists(matrix):
        """
        Comprueba que es una lista de listas 
        """
        result = True
        # Comprueba que es lista de listas 
        if  (isinstance(matrix, list)) and (len(matrix) > 0):
            for i in matrix: # dentro contiene listas
                if isinstance(i,list):
                    result = result and True
                else:
                    result = result and False 
        else:
            result = result and False
        return result
    
    
    def lists_are_same_size(matrix):
        """
        Función que comprueba que las filas de la matriz son del mismo tamaño
        """
        res = True
        aux = matrix[0]
        try:
            for i in matrix:
                if len(i) == len(aux):
                    res = res and True
                else:
                    res = res and False
            aux = i

        except TypeError: 
            print("The matrix is a List, not a List of Lists")
        
        if(res == False): 
            print("Rows of the matrix are not the same size")
        return res


    def all_elements_are_numbers(matrix):
        """
        Comprueba que todos los elementos de la matriz son numeros 
        """
        result = True
        for i in matrix:
            for j in i:
                result = result and (isinstance(j, int) or isinstance(j, float))
        return result

    is_list = input_is_list_of_lists(matrix)
    is_size = lists_are_same_size(matrix)
    is_number = all_elements_are_numbers(matrix)

    return is_list and is_size and is_number# Katas

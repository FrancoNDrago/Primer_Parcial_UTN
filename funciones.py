import csv
import json
import random



def cargar_csv(ruta_csv):
    datos_csv = []
    """
    Carga el archivo csv y devuelve este en formato de lista de diccionarios.
    
    Parametro: Ruta del archivo csv.
    Retorna: Las filas del archivo csv en una lista de diccionarios.
    """
    try:
        with open(ruta_csv, mode="r", encoding="utf-8") as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for linea in lector_csv:
                datos_csv.append(linea)
        print("El archivo csv se cargo con exito.")
    except FileNotFoundError:
        print(f'No se encontro el archivo "{ruta_csv}". Corrobore que el nombre del archivo y la ruta sean correctos.')
    except Exception:
        print(f"Ocurrio un error al cargar el archivo csv {Exception}")
        
    return datos_csv                


def imprimir_lista(datos_csv):
    """
    Itera sobre los diccionarios y los imprime uno por uno.
    
    Parametro: Las listas de diccionarios.
    Retorna: Imprime dicha listas.
    """
    for post in datos_csv:
        print(post)


def asignar_valores(posts):
    """
    Asigna valores aleatorios definidos a las columnas de "Followers", "Likes" y "Dislikes" de cada uno de los posts.
    
    Parametro: Los posts del archivo en forma de lista de diccionarios.
    Retorna: Devuelve la lista de diccionarios con los valores aleatorios asignados.
    """
    for post in posts:
        post["followers"] = random.randint(300, 3000)
        post["likes"] = random.randint(300, 3500)
        post["dislikes"] = random.randint(10000, 20000)
    
    return posts    


def mostrar_mejores_posts(lista, dato):
    """
    Recorre la lista de post y devuelve el post con mayores valores en una estadistica en particular.
    
    Parametros: Posts en forma de lista de diccionarios. 
    La columna de la estadistica.
    
    Retorna: Lista con los usuarios y los valores de estaditicas asignados.
    """
    valor_mayor = 0
    lista_mayor = []
    
    for post in lista:
        if dato in post:
            valor_estadistica = int(post[dato])
            if valor_estadistica >= 2000:
                if valor_estadistica > valor_mayor:
                    valor_mayor = valor_estadistica
                elif valor_estadistica == valor_mayor:
                    lista_mayor.append("{0}: {1}".format(post["user"], valor_mayor))     
                    
    return lista_mayor                


def mostrar_mejores_haters(lista):
    """
    Muestra los posts que tienen valores de dislikes superiores a valores de likes.
    
    Parametro: Posts en forma de lista de diccionarios.
    Retorna: Devuelve la lista de usuarios con más dislikes que likes.
    """
    post_haters = []
    for post in lista:
        if int(post["dislikes"]) > int(post["likes"]):
            post_haters.append("{0}: {1}".format(post["user"], post["dislikes"]))
    return post_haters            


def guardar_post_archivo(posts, nombre_archivo):
    """
    Guarda la lista de posts en un archivo.
    
    Parametros: Los posts del archivo en forma de lista de diccionarios.
    El nombre del archivo donde se guardan los posts.
    
    Retorna: No retorna nada, simplemente guarda lo dicho.
    """
    with open(nombre_archivo, "w") as guardar_post_archivo:
        for post in posts:
            guardar_post_archivo.write(f"{post}\n")
            

def calcular_promedio(lista):
    """
    Calcula el promedio de followers, dividiendo la suma total por la cantidad de posts.
    
    Parametro: Posts en forma de lista de diccionarios.
    Retorna: El promedio de los followers despues de hacer la división.
    """
    cantidad_followers = 0
    for post in lista:
        cantidad_followers += int(post["followers"])
    cantidad_followers_promedio = cantidad_followers // len(lista) 
    return cantidad_followers_promedio    


def ordernar_usuarios(datos, nombre_archivo):
    """
    Ordena los nombres de los usuarios de manera ascendente y guarda estos en un JSON.
    
    Parametros: Lista de diccionarios con información de los usuarios.
    Retorna: Nombre del JSON donde se guardarán los datos ordenados.
    """
    if len(datos) == 0:
        print("No existen datos para ordenar")    
        return
    
    datos_ordenados = sorted(datos, key = lambda x : x["user"])
    with open(nombre_archivo, mode = "w") as archivo:
        json.dump(datos_ordenados, archivo, indent = 4)
    print(f"el archivo {nombre_archivo} fue generado con éxito.")             
    
    
def mostrar_populares(datos):
    """
    Devuelve quien es el usuario con mayor cantidad de likes.
    
    Parametro: Lista de diccionarios con información de los usuarios.
    Retorna: Solo retorna en caso de que no hayan datos.
    """
    if len(datos) == 0:
        print("No existen datos para ordenar")
        return
    
    mayores_likes = max(int(post["likes"]) for post in datos)
    usuarios_populares = [post["user"] for post in datos if int(post["likes"]) == mayores_likes]
    print(f"Usuarios con mayores likes {mayores_likes}: {", ".join(usuarios_populares)}")
    

def mostrar_menu():
    print("---- MENU ----")
    print("1 - Cargar el archivo csv.")
    print("2 - Imprimir la lista.")
    print("3 - Crear estadisticas random.")
    print("4 - Filtrar mejores posts.")
    print("5 - Filtrar por haters.")
    print("6 - Mostrar el promedio followers.")
    print("7 - Ordenar usuarios en forma ascendente.")
    print("8 - Mostrar el mas popular.")
    print("9 - Salir.")    
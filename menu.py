from funciones import *

while True:
    mostrar_menu()
    opciones = input("Ingrese una de las opciones: ")
    
    match opciones:
        case "1":
            ruta_archivo = input("Ingrese la ruta del archivo csv: ")
            datos = cargar_csv(ruta_archivo)
            print("El archivo csv fue cargado exitosamente!")
        case "2":
            imprimir_lista(datos)
        case "3":
            if datos:
                    datos = asignar_valores(datos)
                    print("Valores aleatorios asignados exitosamente.")
        case "4":
            mejores_post = mostrar_mejores_posts(datos, "likes")
            print(mejores_post)
            guardar_post_archivo(mejores_post, 'mejores_posts.csv')
        case "5":
            dislikes = mostrar_mejores_haters(datos)
            print(dislikes)
            guardar_post_archivo(dislikes, "haters.csv")
        case "6":
            promedio_folowers = calcular_promedio(datos)
            print(promedio_folowers)
        case "7":
            nombre_archivo = input("Ingrese el nombre del archivo JSON para poder guardar los datos ordenados: ")
            ordernar_usuarios(datos, nombre_archivo)
        case "8":
            mostrar_populares(datos)
        case "9":
            exit()
        case _:
            print("Ingrese una opción valida!")
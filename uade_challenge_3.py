import random
import os

#arco, arco_con_arc, arco_atajado, menu inicio son graficos y textos para la interfaz del programa
arco="""
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|         1         |        2          |        3          |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|         4         |        5          |        6          |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|         7         |        8          |        9          |
|                   |                   |                   |

Seleccione algunos de los siguientes sectores para atajar: """

arco_con_arc = """

+-------------------+-------------------+-------------------+
|                   |                   |                   |
|          1        |         2         |         3         |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|          4        |      5 (∵)        |         6         |
|                   |        /|\        |                   |
+-------------------+-------/-|-\-------+-------------------+
|                   |         ∧	        |                   |
|          7        |      8 / \        |         9         |
|                   |       /   \       |                   |

Seleccione algunos de los siguientes sectores para patear: """

arco_atajado = """
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|                   |                   |                   |
|                   |                   |                   |
+-------------------+-------------------+-------------------+
|                   |                   |                   |
|                   |        (∵)/@      |                   |
|                   |         |/ /      |                   |
+-------------------+---------|-/-------+-------------------+
|                   |         |         |                   |
|                   |        / \        |                   |
|                   |       /   \       |                   |
"""

menu_inicio = """
      Bienvenido a penales entre Argentina y Paises bajos.
      
      Se iran intercambiando de uno a uno los turnos.

      Debera escribir el numero de la casilla en la que quiere atajar o disparar el penal.
      """

#Funcion para limpiar consola 
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')



#funcion especifica para validar los datos ingresados 
def ingreso_datos(lugar):
    while True:
        if lugar.isdigit():
            lugar = int(lugar)
            if 1 <= lugar <= 9:
                return lugar
            
        lugar=input("ingrese un valor valido, un numero natural entre el 1 y el 9: ") 

#funcion para separara cada sector en el cual se puede atajar/disparar en el arco
#ademas sirve para validar si es gol
def juego(pelota,arquero):
    hitbox = [[1,4,7],[8,5,2],[6,3,9]]
    gol = True
    for i in range(len(hitbox)):
        if pelota in hitbox[i]:
            pelota_location = i
        if arquero in hitbox[i]:
            arquero_location = i

    if arquero_location == pelota_location:
        gol = False
    
    return gol

#funcion para los parametros en los que se basan las reglas de los penales en futbol (normas o leyes)

def jugar(goles_maximos = 5):
    #contador para el resultado final
    goles_maquina = 0
    goles_usuario = 0

    #leyes
    while not(abs(goles_usuario - goles_maquina) >= 1) or ((goles_usuario < goles_maximos / 2) and (goles_maquina < goles_maximos / 2)):
        #definir si se metio gol o no + random para la eleccion de la computadora
        #marcador
        print("               argentina: " + str(goles_usuario),"     paises bajos: "+ str(goles_maquina))
        user = input(arco_con_arc)
        user = ingreso_datos(user)
        bot = random.randint(1, 9)
        gol = juego(user,bot)
        limpiar_consola()
        if gol:
            goles_usuario = goles_usuario + 1
            print("""
                    Hiciste el gol!
                  """)
        else:
            print("            argentina: " + str(goles_usuario),"     paises bajos: "+ str(goles_maquina))
            print(arco_atajado)
            print("""
                    Te atajaron la pelota
                  """)
                    #definir si se atajaste o no la pelota + random para la eleccion de la computadora
        
        print("            argentina: " + str(goles_usuario),"     paises bajos: "+ str(goles_maquina))

        user = input(arco)
        user = ingreso_datos(user)
        bot = random.randint(1, 9)
        gol = juego(bot,user)
        limpiar_consola()
     
        if gol:
            goles_maquina = goles_maquina + 1
            print("""
                    No llegaste a atajar la pelota
                  """)
        else:
            print("            argentina: " + str(goles_usuario),"     paises bajos: "+ str(goles_maquina))
            print(arco_atajado)
            print("""
                  Felicidades atajaste la pelota!
                  """)
            input("Toque enter para continuar\n")
        limpiar_consola()

    
    #definir el ganador
    if(goles_maquina < goles_usuario):
        print("El ganador es Argentina")
    else:
        print("El ganador es Paises bajos")
    
    #mostrar los resultados al usuario    
    print("""
    Estos son los resultados: 
          """)
    print("Goles marcados por Paises bajos: ", goles_maquina)
    print("Goles marcados por Argentina: ", goles_usuario)
    
#execucion del codigo
if "__main__" == __name__:
    print(menu_inicio)
    jugar()
from determinar_areaPared import detAreaPared
from determinar_cantLadrillos import detCantLadrillos
from determinar_cantMezcla import detCantMezcla
from determinar_cantCemento import detCantCemento
from determinar_cantArena import detCantArena

# SE INGRESAN LOS DATOS DE LA PARED POR TECLADO
print("----------- CALCULO DE MATERIALES ----------")
longitud = float (input("Ingrese la longitud de la pared en metros: "))
altura = float (input("Ingrese la altura de la pared en metros: "))
ladrilloTipo = int (input("Ingrese un numero según el tipo de ladrillo:\n1 - Ladrillo comun del 12\n2 - Ladrillo hueco del 18\n"))


#   SE ESTABLECEN LOS VALORES SEGÚN EL TIPO DE LADRILLO
match (ladrilloTipo):
    case 1 :
        ancho = 0.12
        volLadrillo = 0.001728
        areaLadConJunta = 0.019125
    case 2 :
         ancho = 0.18
         volLadrillo = 0.0081
         areaLadConJunta = 0.051675

areaPared = detAreaPared(altura,longitud)
cantLadrillos = round(detCantLadrillos(areaPared,areaLadConJunta),2) 
cantMezcla = round(detCantMezcla(areaPared, ancho , volLadrillo ,cantLadrillos),2) 
cantCemento = round(detCantCemento(cantMezcla),2) 
cantArena = round(detCantArena(cantMezcla),2) 

print(areaPared)
print(cantLadrillos)
print(cantMezcla)
print(cantCemento)
print(cantArena)
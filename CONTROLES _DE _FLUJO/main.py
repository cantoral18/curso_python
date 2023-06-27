# ##conversiones string numeros
# numero="10"
# numeroconvertido=int(numero)
# print(type(numero))
# print(type(numeroconvertido))

# flotanteString="10"
# flotanteNumero=float(flotantestring)

# numeroEntero=20
# numeroString=str(numeroEntero)

# print(type(numeroEntero))
# print(type(numeroString))

# ##controles de fujo
# bloques
# cuando nosotros utilicemos cualquier control de flujo o funciones
# el codigo que se debe ejecutar despues debera estar definida por bloques o identificacines
# los programas se manejan de manera secuencial  


# ##control de flujo :
# 1.condicional .. se realiza algo si cumple cietas condiciones 
# cuando es verdad si se ejecuta,resuelve y cuando es falso 
# se salta al siguiente linea

# nombre"maritza"
# mensaje"hola"
# print mensaje
# print nombre


# #match apellido:
# #case apellido if apellido[2]=="e":
# #print(f"bienvenida")
# #case _:
# #print ("tu no eres de esta raza,eres")

# ##BLUCLES
# condicion=0
# wile condicion<11:
#     print(condicion)
#     condicion=condicion+1
    
# #ejercicio 1 pedir numeros pares:
# condicion=2
# while condicion<2
#     print(condicion)
#     condicion=condicion+2

# #ejercicio2 
# edad=0
# while edad !=20:
#     edad=int(input("ingrese edad: "))

# #ejercicio3
# nombre=" "
# while nombre !=si:
#     nombre=input("ingese nombre: ")
# #otra forma de hacer:
# while True:
# nombre=input("como te llamas")
# if nombre =="si:"
#     break

# #for numero in range(0,10):
# # print (numero)

# vocales=["a","e","i","o","u"]
# for numero in range(0,5):
#     print(vocales[numero])

# for vocal in vocales:
#     print(vocal)

## crear una lista de cinco colores




# colores=["azul","amarillo","rojo","negro","blanco"]

# for color in colores:
#     if color =="rojo":
#         print( "encontrado" )
#         break
#     print(color)
        
# Lista=[]
# print(Lista)
# primerDato=input("ingese una fruta: ")
# Lista.append(primerDato)
# print(Lista)
# segundoDato=input("ingrese una segunda fruta: ")
# Lista.append(segundoDato)
# print(Lista)


##CREAR UN PROGRAMA QUE ME DEJE INGRESAR DATYOS EN UNA LISTA VACIA
##EN CASO DEL USUARIOO INGRESE LA PALABRA "SI" EL PROGRAMA DEJARA
##DE PEDIR DATOS Y ME MOSTRARARA LA LISTA  CON TODO LOS DATOS INGRESADOS
# Lista=[ ]
# letras=input("ingese una letra")
# while letras!="si":
#     Lista.append(letras)
#     letrsias=input("ingese una letra")
# print(Lista)    

# lista=[]
# condicion=1
# while condicion:
#     pedirDato=input("ingese un dato ")
#     if pedirDato == "si":
#         condicion=0
#     lista.append(pedirDato)    
#     print(lista)

## TAREA DE 5 LISTAS 
## 1
# Lista=[]
# for dato in range(5):
#     dato=input("ingrese numero: ")
#     Lista.append(dato)
# print(Lista)
## 2
 ## PEDIR AL USUARIO UN NUMERO LUEGO GENERAR LA TABLA DE MULTIPLICAR
## DE DICHO NUMERO DEL 1 HASTA EL 12

# tablaDe=int(input("ingese un numero: "))
# for numero in range (1,13):
#      resultado=numero*tablaDe
#      print (f"{numero} * {tablaDe}= ¨{resultado} ")


## un programa que me pida un numero y me calcule su factorial



numero=int(input("ingese un numero: "))
factorial=1
for num in range(1,numero+1):
    factorial=factorial*num
print(factorial)

## tarea mostrar las sucecion fibocci de los 10 primeros numeros
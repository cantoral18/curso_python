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



# numero=int(input("ingese un numero: "))
# factorial=1
# for num in range(1,numero+1):
#     factorial=factorial*num
# print(factorial)

# ## tarea mostrar las sucecion fibocci de los 10 primeros numeros
# ##pedir un usuario una lista de 5 de elementos si en la  lista contiene la palabra disco
# #mostrar la palabra y la ubicacion de su indice positivo

# Lista=[]
# indice=0
# palabra=""
# while len(Lista)<5:
#     dato=input("ingresa un dato")
#     Lista.append(dato)
# for texto in range(0,len(Lista)):
#     if Lista[texto] =="disco":
#         palabra=Lista[texto]
#         indice=texto
# print(f"""el texto disco se encuentra en el indice hola{indice}
#        y el texto es {palabra}
#     """)


# frutas=[]
# while len(frutas)<5:
#     nuevafruta=input("ingrese una fruta: ")
#     for fruta in frutas:
#         if len(nuevafruta)==len  (frutas):
#             print("misma longuitud ingrese otro: ")
#     if nuevafruta in frutas:
#         print("esta fruta ya existe ingrese otro")
#     else:
#         frutas.append(nuevafruta)

# def textolargo(array):
#     longitudTexto=0
#     mostrarfruta=""
#     for index in range(0,len(array)):
#         if  len(array[index])>longitudTexto:
#             longitudTexto=len(array[index]) 
#             mostrarfruta=array[index]
#     return mostrarfruta

# print(textolargo(frutas))

# frutas=[]
# while len(frutas)<5:
#     nuevafruta=input("ingrese una fruta: ")
#     for fruta in frutas:
#         if len(nuevafruta)==len  (frutas):
#             print("misma longuitud ingrese otro: ")
#     if nuevafruta in frutas:
#         print("esta fruta ya existe ingrese otro")
#     else:
#         frutas.append(nuevafruta)

# def textolargo(array):
#     longitudTexto=0
#     mostrarfruta=""
#     for index in range(0,len(array)):
#         if  len(array[index])>longitudTexto:
#             longitudTexto=len(array[index]) 
#             mostrarfruta=array[index]
#     return mostrarfruta

# # print(textolargo(frutas))
# # ... para el examen
#  ##pa saber indice
# # lista=["a","e","i"]
# # for indice in range(0,len(lista)) :
# #  print (indice)

# #  # valor y indice
# #  lista=["a","e","i"]
# # for indice in valor in enumerate(lista)
# #  print (indice,valor)

# # ##sacar  solo una de las letras
# #  lista=["a","e","i"]
# # for _,valor in enumerate(lista):
# #     if valor =="i":
# #          print (valor)

# ##crear una lista de numeros del 1 al 10crear una funcion que nos permita recibir como parametro una lista 
# ##la funcion tendra que retornar un nuevo aray con todo los numero paraes que existe 

# lista=["1","2","3","4","5","6","7","8","9","10"]

# def numeros_pares(lista):
#     nueva_lista=[]
#     for _,num in enumerate(lista):
#         if num%2==0:
#             nueva_lista.append(num)
#     return nueva_lista
# print(numeros_pares(lista))
# ## hacer un programa que pida al usuario un texto, y evaluar con una funcion  la cantidad de vocales a que tiene el texto.

# letra=[]

## de la galeria de productos ,el usuario i
# De la galería de productos, el usuario introducirá el código 
# y el número de unidades del producto que desea comprar. 
# El programa determinará el total a pagar, como una factura.
# Una variante a este ejercicio que lo haría un poco más complejo 
# sería dar la posibilidad de seguir ingresando diferentes códigos de 
# productos con sus respectivas cantidades, y cuando el usuario desee 
# terminar el cálculo de la factura completa con todas sus compras. Te animas??
# '''

print("Elija el producto deseado: ")
print("Producto\t\t\tCódigo")
print("Camisa\t\t\t\t  1")
print("Pantalon\t\t\t  2")
print("Falda\t\t\t\t  3")

cuenta = []
precios = [100, 120, 100]

comprando = 0
while comprando == 0:

	codigo = input("Introduzca el código del articulo: ")
	cantidad = input("Introduzca la cantidad de articulos: ")
	cuenta.append((precios[codigo-1])* cantidad)
	comprando = input("Para agregar otro articulo 0 para salir 1: ")
precio_total =0
for precios in cuenta:
	precio_total=precio_total+ precios
print("el precioa pagar es de " + str(precio_total))


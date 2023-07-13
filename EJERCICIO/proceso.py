import ingresa_datos

while len(ingresa_datos.Lista)<5:
    dato = input("ingresa un dato:")
    ingresa_datos.Lista.append(dato)
for texto in range(0,len(ingresa_datos.Lista)):
    if ingresa_datos.Lista [texto] =="disco":
        palabra=ingresa_datos.Lista[texto]
        indice=texto
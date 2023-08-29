correr=input("¿cuanto espacios se corren las letras?: ")
correr=int(correr)
abcdario="abcdefghijklmnñopqrstuvwxyz"
dia= 1
for i in range(5):
    print("Ingresa mensaje dia ",dia)
    mensaje=input("")
    contador=0
    mensajecif=""
    for j in mensaje:
        if (j==" "):
             mensajecif=mensajecif+" "    
        else:
            mensajecif=mensajecif+abcdario[(abcdario.find(j)+correr)%27]

    print(mensajecif)

        
      


    
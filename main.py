#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Hola! Bienvenido a la Ronda 2. Manos a la obra y Ã©xitos!
#Cuando finalicen las consignas del desafÃ­o de la Ronda, guarden su cÃ³digo en su disco local con las imÃ¡genes que utilizaron
#Suban en la "Plataforma de la MaratÃ³n" su proyecto en formato ZIP, comprimiendo los documentos necesarios para ejecutar el cÃ³digo

#Cargamos las librerias necesarias
import turtle
from funciones import *

import os.path
import time
import tkSimpleDialog

from datetime import datetime


#Cargamos los recursos de imagenes. Primero se deben subir y activar a Trinket
screen = turtle.Screen()
screen.register_shape("organico.gif")
screen.register_shape("vidrio.gif")
screen.register_shape("lata.gif")
screen.register_shape("otros.gif")
screen.register_shape("papel.gif")
screen.register_shape("toxico.gif")
screen.register_shape("robotuno.gif")
screen.register_shape("manzana.gif")
screen.register_shape("robotdos.gif")
screen.register_shape("dirtystreet.gif")
screen.register_shape("patacerdo.gif")
screen.register_shape("pescado.gif")
#Cargamos las imagenes de la basura radioactiva
screen.register_shape("organicoR.gif")
screen.register_shape("vidrioR.gif")
screen.register_shape("lataR.gif")
screen.register_shape("otrosR.gif")
screen.register_shape("papelR.gif")
screen.register_shape("toxicoR.gif")
screen.register_shape("manzanaR.gif")
screen.register_shape("patacerdoR.gif")
screen.register_shape("pescadoR.gif")


#Inicializamos variables
puedoConfigurar=True
jugando = False
situada = False
patronMovimiento='aleatorio'  
modoDeJuego='porTiempo'

global NombreJugador, PPpuntos, PTpuntos, JuegoOrganico
global txtInstrucciones, Pantalla, Score, cartel,CartelOrganico
tiempoTotalConfigurado=15
puntosTotalesConfigurados=300
nombreJugador='Jug1'
tiempoTotal=tiempoTotalConfigurado
puntosTotales=puntosTotalesConfigurados
tiempoActual=0
puntosActuales=0
tiempocartel=0
cartel=turtle.Turtle()
JuegoOrganico='NO'
CartelOrganico=turtle.Turtle()
CartelScores=turtle.Turtle()
NombreJugador=tkSimpleDialog.askstring("Bienvenido al Juego","Ingresa tu Nombre:")


def mostrarMenu():
  global txtInstrucciones, puedoConfigurar,JuegoOrganico, NombreJugador, jugador
  


 
  jugador=obtenerJugador()

  txtInstrucciones = turtle.Turtle()
  txtInstrucciones.clear()
  txtInstrucciones.hideturtle()
  txtInstrucciones.speed(0)
  txtInstrucciones.penup()

  txtInstrucciones.setx(-240)
  txtInstrucciones.sety(50)
  txtInstrucciones.right(90)
  
  txtInstrucciones.forward(-150)
  txtInstrucciones.color("LightBlue")
  txtInstrucciones.write("  Juego Reciclemos Juntos "+NombreJugador,  font=("Times", 24, "bold"))

  
  txtInstrucciones.forward(60)
  txtInstrucciones.color("lightblue")
  txtInstrucciones.write("Mueve el robot con las flechas para recolectar los residuos", font=("Times", 13, "bold"))
  
  
  txtInstrucciones.forward(70)
  txtInstrucciones.color("lightblue")
  txtInstrucciones.write("Menu", font=("Times", 18, "bold"))
  txtInstrucciones.forward(40)
  txtInstrucciones.color("LightBlue")
  txtInstrucciones.write("t - Empezar juego por tiempo", font=("Times", 13, "bold"))
  txtInstrucciones.forward(30)
  txtInstrucciones.write("p - Empezar juego por puntos", font=("Times", 13, "bold"))
  txtInstrucciones.forward(30)
  txtInstrucciones.write("q , e , z , c - diagonales", font=("Times", 13, "bold"))
  txtInstrucciones.forward(30)
  txtInstrucciones.write("x - Salir del juego y volver al menu", font=("Times", 13, "bold"))
  txtInstrucciones.forward(30)
  txtInstrucciones.write("c - Configuracion del juego", font=("Times", 13, "bold"))
  txtInstrucciones.forward(30)
  txtInstrucciones.color("green")
  txtInstrucciones.write("o - Modo Organico", font=("Times", 13, "bold"))


  
  
  puedoConfigurar = True
  screen.update()
  #Configuramos los dos modos de juego (Organico activado y desactivado)
  if(JuegoOrganico=='SI'):
    MODO="ACTIVADO"
  
    
  else:
    MODO="DESACTIVADO"


 
 
  CartelOrganico.clear()
  CartelOrganico.hideturtle()
  CartelOrganico.penup()
  CartelOrganico.setx(-250)
  CartelOrganico.sety(-250)
 #Caracterizamos al cartel
  CartelOrganico.color("Red")
  CartelOrganico.write("MODO ORGANICO:" + MODO, font=("Times", 16, "bold"))

  if os.path.exists("PPScore.txt"):  
      CartelScores.clear()
      CartelScores.hideturtle()
      CartelScores.penup()
      CartelScores.setx(250)
      CartelScores.sety(-100)
     #Caracterizamos al cartel
      CartelScores.color("Blue")
      CartelScores.write("TOP 5 BEST!" , font=("Verdana", 16, "bold"))


      TT=open("PPScore.txt","r")

      ScoreTop=TT.readline()

      Listado=ScoreTop.split(";")

      TT.close()
      if len(ScoreTop)>0:
        CartelScores.setx(235)
        CartelScores.sety(-130)
        bajar=0
        cuentalinea=1
        for DatoScore in Listado:
          CartelScores.sety(-130+bajar)
          CartelScores.write(DatoScore , font=("Verdana", 12, "bold"))
          bajar=bajar-30  
          cuentalinea=cuentalinea+1
          if cuentalinea>5:break
      
  
mostrarMenu()



#Definimos al bucle del juego
def loopJuego():
  global jugando, txtInstrucciones, situada, jugador, patronMovimiento, puedoConfigurar, modoDeJuego, tiempoTotal, puntosTotales, puntosActuales, nombreJugador
  global tiempocartel, JuegoOrganico, CartelOrganico

  txtInstrucciones.clear()
  CartelOrganico.clear()
  CartelScores.clear()

  screen = turtle.Screen()
  screen.bgpic("dirtystreet.gif")
  
  cronometro=obtenerCronometro()
  puntuador=obtenerPuntuador()
  
  txtTiempoRestante=obtenerTxtTiempoRestante()
  txtTiempoRestante.color("white")

  txtTiempoRestante.write('Tiempo: ', font=("Times", 19, "bold"))
  txtPuntos=obtenerTxtPuntos()
  
  txtPuntos.color("white")

  txtPuntos.write('Puntos: ', font=("Times", 19, "bold"))
  
  tiempoInicio=int(round(time.time()))
  
  auxTiempo=int(round(time.time()-tiempoInicio))
  auxPuntos=0
  
  if (modoDeJuego=='porTiempo'):
    puntosActuales=0
    tiempoRestante=tiempoTotalConfigurado
  elif (modoDeJuego=='porPuntos'):
    puntosActuales=puntosTotalesConfigurados
    puntosRestantes=0
    tiempoRestante=0
  
  
  bas=obtenerBasura(JuegoOrganico)
  
  
  diccionarioPuntaje = {"patacerdo.gif" : "600", "pescado.gif" : "150", "manzana.gif" : "150", "organico.gif" :"200", "otros.gif" : "10", "toxico.gif" : "150", "vidrio.gif" : "75", "lata.gif" : "50", "papel.gif" : "30"}
  
    
  while (jugando == True):
    jugador.shape("robotdos.gif")
    puedoConfigurar=False
    tiempoRestante=int(round(time.time()-tiempoInicio))
    if (modoDeJuego=='porTiempo'):
      
    
      if not (tiempoRestante==auxTiempo):
        cronometro.clear()
        auxTiempo = tiempoRestante
    
      tiempoRestante=tiempoTotal-tiempoRestante
    
    elif (modoDeJuego=='porPuntos'):
      if not (tiempoRestante==auxTiempo):
        cronometro.clear()
        auxTiempo = tiempoRestante
      
      auxPuntos = puntosRestantes
      
    
  
    patrones=['linea', 'aleatorio']
    bas=moverBasura(bas, patronMovimiento)

    
    if (situada==False):
      patronMovimiento=random.choice(patrones)
      situada=True      
    
    bas=moverBasura(bas, patronMovimiento)
    
    bas=reubicarBasuraSiSeVa(bas)
    jugador=reubicarJugadorSiSeVa(jugador)
    
    #aca es donde toma el valor a sumar con NUM
    x=int(bas.xcor())
    if x>40:
      num=0
      if bas.shape()[len(bas.shape())-5:len(bas.shape())]<>"R.gif":
        bas.shape(bas.shape()[0:len(bas.shape())-4]+"R.gif")
              
      #es radioactivo y no debe sumar
    else:


      
      if bas.shape()[len(bas.shape())-5:len(bas.shape())]=="R.gif":
        bas.shape(bas.shape()[0:len(bas.shape())-5]+".gif")



      num=int(diccionarioPuntaje[bas.shape()])


   
    

    

    
    if(int(round(time.time())<=tiempocartel+3)):
        CartelBravo("0")
        jugador.shape("robotdos.gif")
    

    if (colisionan(jugador, bas, 60) == True):
      #al chocar con el residuo, la imagen cambia, simulando que el robot "come" la basura cerrando la boca
      jugador.shape("robotuno.gif")

      situada = False
      bas.hideturtle()
      bas.clear()
      bas=obtenerBasura(JuegoOrganico)
      tiempocartel=int(round(time.time()))

      if num>0:
        CartelBravo("¡BRAVO!")
      else:
        CartelBravo("¡ZONA RADIOACTIVA!")
      
      
      
      if(modoDeJuego=='porPuntos'):
        puntosActuales=puntosActuales-num
        
  
        if (puntosActuales<=0):
          puntosActuales=puntosActuales*-1
          cronometro.clear()
          puntuador.clear()
          jugando=False
  
      else:
        puntosActuales=puntosActuales+num
      
      if not (puntosActuales==auxPuntos):
          puntuador.clear()
          auxPuntos=puntosActuales
        
    if (modoDeJuego=='porTiempo'):  
        if (tiempoRestante<=0):
      
          cronometro.clear()
          jugando=False
    
  
   
     
     
    
       
    dibujarElementosDinamicos(bas, jugador, cronometro, tiempoRestante, puntuador, puntosActuales, modoDeJuego)
    screen.update()
  



  #Si el juego estaÂ¡ detenido borramos todo

    
    
  jugador.hideturtle()
  jugador.clear()
  txtTiempoRestante.clear()
  txtTiempoRestante.hideturtle()
  txtPuntos.clear()
  txtPuntos.hideturtle()
  puntuador.clear()
  puntuador.hideturtle()
  cronometro.clear()
  cronometro.hideturtle()
  bas.hideturtle()
  bas.clear()
  txtInstrucciones.hideturtle()
  txtInstrucciones.clear()
  if(modoDeJuego=='porTiempo'):
    PorPuntos(NombreJugador,puntosActuales)
  elif(modoDeJuego=='porPuntos'):
    PorTiempos(NombreJugador,puntosActuales)
  
  mostrarMenu()
  
  
#Definimos la operacion de comienzo de juego
def empezarJuego():
  global jugando, puedoConfigurar
 
  if (jugando==False):
    jugando = True
    loopJuego()
   
def empezarJuegoPorPuntos():
  global modoDeJuego
  modoDeJuego='porPuntos'
  empezarJuego()

def empezarJuegoPorTiempo():
  global modoDeJuego
  modoDeJuego='porTiempo'
  empezarJuego()

def organico():
  global jugador, JuegoOrganico, txtInstrucciones
  if(JuegoOrganico=='SI'):
    JuegoOrganico='NO'
  else:
    JuegoOrganico='SI' 
  txtInstrucciones.clear()
  jugador.hideturtle()
  mostrarMenu()

def volverAlMenu():
  global jugando, puedoConfigurar
  jugando = False
  puedoConfigurar=False
  
  
def ingresarParametrosDeConfiguracion():
  global tiempoTotal, puntosTotalesConfigurados, puedoConfigurar, jugando, nombreJugador
  
  if (jugando==False):
  
    if (puedoConfigurar==True):
      puedoConfigurar=False
      tiempoTotal= int(raw_input("Ingrese la cantidad de segundos que dispondraÂ¡ el jugador para el Modo por Tiempo"))
      puntosTotalesConfigurados= int(raw_input("Ingrese el puntaje maximo para el Modo Puntos"))
      
      if not (tiempoTotal > 0):
        tiempoTotal=10
      if not (puntosTotalesConfigurados > 0):
        puntosTotalesConfigurados=5




    
  
#Funciones de puntos
def MostrarTT():
  global txtScores
  
  txtScores = turtle.Turtle()

  TT=open("TTscore.txt","r")

  Score=TT.read()

  TT.close()

  Listado=Score.split(";")


  c=0

  txtScores.hideturtle()
 
  txtScores.speed(0)
  txtScores.setx(-240)
  txtScores.sety(40)
  txtScores.right(90)

  txtScores.forward(-150)
  txtScores.color("LightBlue")
  txtScores.write("Mejores Cinco Puntajes !",  font=("Times", 24, "bold"))


  
  txtScores.color("LightBlue")
  
  #mostramos los ultimos 5 juegos que registraron score
  for LS in Listado:
    
    txtScores.forward(40)
    txtScores.write("               "+LS,font=("Times", 20, "bold"))
    c=c+1
    
    if(c==5):
      break




  time.sleep(5)
  txtScores.clear()

def MostrarPP():
  txtScores = turtle.Turtle()

  PP=open("PPscore.txt","r")

  Score=PP.read()

  PP.close()

  Listado=Score.split(";")


  c=0

  
  txtScores.setx(-240)
  txtScores.sety(40)
  txtScores.right(90)

  txtScores.forward(-150)
  txtScores.color("Green")
  txtScores.write("Mejores Cinco Puntajes !",  font=("Times", 24, "bold"))


  
  txtScores.color("LightBlue")
  txtScores.hideturtle()
 
  txtScores.speed(0)
  #mostramos los ultimos 5 juegos que registraron score
  for LS in Listado:
    
    txtScores.forward(40)
    txtScores.write("               "+LS,font=("Times", 20, "bold"))
    c=c+1
    
    if(c==5):
      break




  time.sleep(5)
  txtScores.clear()
    

    
 
#Funcion para agregar ceros delante para ordenar luego
  
def AgregarCeros(pPuntaje):
  numero=str(pPuntaje)
  cifras=len(numero)
  for Ceros in range (0,7-cifras):
    numero="0"+numero
    
  return numero 

  
def PorPuntos(NJugador, Puntaje):

  PP=open("PPscore.txt","a")

  

  PP.write(AgregarCeros(Puntaje)+"-"+NJugador+";")

  PP.close()

  
  #lee el archivo para luego ordenar todos los datos
  PP=open("PPscore.txt","r")

  Score=PP.read()
  #Le sacamos el ultimo caracter porque sino el split toma el punto y coma dos veces
  Score=Score[0:len(Score)-1]
  
  PP.close()



  Listado=Score.split(";")



  Listado=sorted(Listado)
 

  
  Listado.reverse()


  #escribimos todos los datos ordenados
  PP=open("PPscore.txt","w")

  for dato in Listado:
    PP.writelines(dato+";")
  PP.close()

  MostrarPP()




  
def PorTiempos(NJugador, Puntaje):
  PP=open("TTscore.txt","a")

  

  PP.write(AgregarCeros(Puntaje)+"-"+NJugador+";")

  PP.close()

  
  #lee el archivo para luego ordenar todos los datos
  PP=open("TTscore.txt","r")

  Score=PP.read()
  #Le sacamos el ultimo caracter porque sino el split toma el punto y coma dos veces
  Score=Score[0:len(Score)-1]
  
  PP.close()



  Listado=Score.split(";")



  Listado=sorted(Listado)
 

  
  #Listado.reverse() No se reversa porque el mejor es quien menos puntos tiene... como en el chinchon!


  #escribimos todos los datos ordenados
  PP=open("TTscore.txt","w")

  for dato in Listado:
    PP.writelines(dato+";")
  PP.close()
  

    
  MostrarTT()


        
#Definimos las funciones de movimiento del jugador
def atras():
  global jugador
  if jugador.ycor()>-180:
    jugador.sety(jugador.ycor()-30)

def adelante():
  global jugador
  if jugador.ycor()<173:
   jugador.sety(jugador.ycor()+30)
  
def izquierda():
    global jugador
    if jugador.xcor()>-250:
     jugador.setx(jugador.xcor()-30)
    
def derecha():
    global jugador
    if jugador.xcor()<265:
     jugador.setx(jugador.xcor()+30)
    
def salirDelJuego():
  global jugando
  jugando=False

def diagonalarribaderecha():
    global jugador
    if jugador.xcor()<180 and jugador.ycor()<173:
      jugador.setx(jugador.xcor()+20)
      jugador.sety(jugador.ycor()+20)
def diagonalarribaizquierda():
  global jugador
  if jugador.xcor()>-180 and jugador.ycor()<173:
    jugador.setx(jugador.xcor()-20)
    jugador.sety(jugador.ycor()+20)
def diagonalabajoderecha():
  global jugador
  if jugador.xcor()<180 and jugador.ycor()>-173:
    jugador.setx(jugador.xcor()+20)
    jugador.sety(jugador.ycor()-20)
def diagonalabajoizquierda():
  global jugador
  if jugador.xcor()>-180 and jugador.ycor()>-173:
    jugador.setx(jugador.xcor()-20)
    jugador.sety(jugador.ycor()-20)

def CartelBravo(Texto):
    
    cartel.clear()
    cartel.hideturtle()
    cartel.speed(0)
    cartel.penup()
   
    
    if(Texto=="0"):
        cartel.clear()
    else:
       if Texto=="¡BRAVO!":
         cartel.color("Yellow")
         cartel.penup()
         cartel.setposition(-100,0)
       else:
         cartel.color("Green")
         cartel.penup()
         cartel.setposition(-200,0)

       cartel.write(Texto,font=("Times", 25, "bold"))
      
    screen.update()

    

    
#Realizamos codigo que invoca las funciones anteriores segun la tecla que se presione  

turtle.onkey(adelante, "Up")
turtle.onkey(atras, "Down")
turtle.onkey(izquierda, "Left")
turtle.onkey(derecha, "Right")
turtle.onkey(empezarJuegoPorPuntos, "p")
turtle.onkey(empezarJuegoPorTiempo, "t")
turtle.onkey(ingresarParametrosDeConfiguracion, "c")
turtle.onkey(salirDelJuego, "x")
turtle.onkey(organico, "o")
turtle.onkey(diagonalarribaderecha, "e")
turtle.onkey(diagonalarribaizquierda, "q")
turtle.onkey(diagonalabajoderecha, "c")
turtle.onkey(diagonalabajoizquierda, "z")
turtle.listen()
turtle.mainloop()



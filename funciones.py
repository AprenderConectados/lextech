#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Cargamos las librerÃ­as necesarias
import turtle
import random
import math

#Se realizan funciones de apoyo para que el main.py con nombres bien representativos

def dibujarElementosDinamicos(basura, jugador, cronometro, tiempoActual, puntuador, puntosActuales, modoDeJuego):
  
  if tiempoActual > 0:
    cronometro.color("white")
    cronometro.write(tiempoActual, font=("Times", 16, "bold"))
    
  if puntosActuales > 0:
    puntuador.color("white")

    puntuador.write(puntosActuales, font=("Times", 16, "bold"))

  basura.showturtle()
  jugador.showturtle()  

      
def moverBasura(basura, patronMovimiento):
  basura.penup()
  
  if (patronMovimiento=='linea'):
    basura.forward(0.7)
 
  if (patronMovimiento=='aleatorio'):
    basura.right(random.randint(-180,180))
    basura.forward(25)
    basura.setx(basura.xcor()+random.randint(-20,20))
    basura.sety(basura.ycor()+random.randint(-20,20))


 # x=int(basura.xcor())
 # if x>40:
 #   imgs = ["manzanaR.gif", "organicoR.gif", "vidrioR.gif", "lataR.gif", "otrosR.gif", "papelR.gif", "toxicoR.gif", "pescadoR.gif", "patacerdoR.gif"]
 #   print "RADIOACTIVO"
  return basura

def obtenerBasura(Modo):
  if(Modo<>'SI'):
      imgs = ["manzana.gif", "organico.gif", "vidrio.gif", "lata.gif", "otros.gif", "papel.gif", "toxico.gif", "pescado.gif", "patacerdo.gif"]
  else:
      imgs = ["organico.gif", "manzana.gif", "pescado.gif", "patacerdo.gif"]

  
  imgActual=random.choice(imgs)
  basura = turtle.Turtle()
  basura.hideturtle()
  basura.shape(imgActual)
  basura.penup()
  basura.goto(random.randint(-180,180),random.randint(-180,180)) 
  return basura
  

def obtenerJugador():
  jugador=turtle.Turtle()
  jugador.shape("robotuno.gif")
  jugador.penup()
  jugador.setx(145)
  jugador.sety(0)
  return jugador
  
def obtenerCronometro():
  tiempoRestante=turtle.Turtle()
  tiempoRestante.penup()
  tiempoRestante.hideturtle()
  tiempoRestante.setx(-80)
  tiempoRestante.sety(170)
  
  return tiempoRestante
  
def obtenerPuntuador():
  puntuador=turtle.Turtle()
  puntuador.penup()
  puntuador.hideturtle()
  puntuador.setx(-80)
  puntuador.sety(144)
 
  
  return puntuador
  
def obtenerTxtTiempoRestante():
  txtTiempoRestante=turtle.Turtle()
  txtTiempoRestante.penup()
  txtTiempoRestante.hideturtle()
  txtTiempoRestante.setx(-190)
  txtTiempoRestante.sety(170)
  return txtTiempoRestante 
  
def obtenerTxtPuntos():
  txtPuntos=turtle.Turtle()
  txtPuntos.penup()
  txtPuntos.hideturtle()
  txtPuntos.setx(-190)
  txtPuntos.sety(145)
  return txtPuntos   

def reubicarBasuraSiSeVa(bas):
    x = bas.xcor()
    y = bas.ycor()
    
    if x > 150:
      bas.setx(150)
    elif x < -180:
      bas.setx(-150)
    if y > 180:
      bas.sety(150)
    elif y < -180:
      bas.sety(-150)
    return bas

def reubicarJugadorSiSeVa(jug):
    x = jug.xcor()
    y = jug.ycor()
    
    if x > 160:
      jug.setx(160)
    elif x < -160:
      jug.setx(-160)
  
    if y > 160:
      jug.sety(160)
    elif y < -165:
      jug.sety(-165)
    return jug

def colisionan(obj, jugador, umbral):


  d=math.sqrt(math.pow(obj.xcor()-jugador.xcor(),2)+math.pow(obj.ycor()-jugador.ycor(),2))


  if d < umbral:
    return True
  else:
    return False
 

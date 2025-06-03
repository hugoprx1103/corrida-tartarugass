import turtle
import random

tela = turtle.Screen()
tela.bgcolor("lightblue")

cores = ['red', 'blue', 'green', 'orange']
tartarugas = []

for cor in cores:
    t = turtle.Turtle()
    t.color(cor)
    t.shape('turtle')
    t.penup()
    t.goto(-160, 100 - cores.index(cor) * 50)
    t.pendown()
    tartarugas.append(t)

for passo in range(100):
    for t in tartarugas:
        t.forward(random.randint(1, 5))

tela.exitonclick()

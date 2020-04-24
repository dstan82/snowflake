import turtle
import tkinter as tk

root = tk.Tk()

#turtle.speed("slow")	
turtle.pencolor("white")
turtle.pensize(20)
turtle.shape("turtle")

turtle.Screen().bgcolor("red")

def vsnow():
	
	turtle.right(30)
	turtle.forward(150)
	turtle.backward(150)
	turtle.left(60)

	turtle.forward(150)
	turtle.backward(150)
	turtle.right(30)

def snowArm():
	for i in range(4):
		turtle.forward(150)
		vsnow()
	turtle.backward(600)

def snowFlake():
	for x in range(6):
		snowArm()
		turtle.right(60)

snowFlake()

#for i in range (4):

#	turtle.forward(100)
#	vsnow()
#	turtle.backward(400)

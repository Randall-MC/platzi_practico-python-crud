import turtle

# Configurar la ventana
window = turtle.Screen()
window.bgcolor("sky blue")

# Configurar la tortuga
t = turtle.Turtle()
t.speed(0)  # La velocidad más rápida
t.left(90)
t.backward(100)

# Definir la función recursiva para dibujar un fractal de montaña
def mountain(t, length, depth):
    if depth == 0:
        t.color("green")
        t.forward(length)
    else:
        t.color("brown")
        mountain(t, length / 2, depth - 1)
        t.right(120)
        mountain(t, length / 2, depth - 1)
        t.left(60)
        mountain(t, length / 2, depth - 1)
        t.right(120)
        mountain(t, length / 2, depth - 1)
        t.left(60)

# Dibujar la montaña
mountain(t, 200, 4)

# Mantener abierta la ventana hasta que el usuario la cierre
turtle.done()
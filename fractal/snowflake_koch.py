import turtle

# Configurar la ventana
window = turtle.Screen()
window.bgcolor("sky blue")

# Configurar la tortuga
sf = turtle.Turtle()
sf.speed(0)  # La velocidad más rápida
sf.color("white")

# Definir la función recursiva para dibujar un copo de nieve de Koch
def snowflake(sf, length, depth):
    if depth == 0:
        sf.forward(length)
    else:
        snowflake(sf, length / 3, depth - 1)
        sf.left(60)
        snowflake(sf, length / 3, depth - 1)
        sf.right(120)
        snowflake(sf, length / 3, depth - 1)
        sf.left(60)
        snowflake(sf, length / 3, depth - 1)

# Dibujar los copos de nieve
positions = [(-400, 400), (200, 0), (-200, -100)]
for position in positions:
    sf.penup()
    sf.goto(position)
    sf.pendown()
    sf.begin_fill()
    for _ in range(3):
        snowflake(sf, 200, 4)
        sf.right(120)
    sf.end_fill()

# Mantener abierta la ventana hasta que el usuario la cierre
turtle.done()
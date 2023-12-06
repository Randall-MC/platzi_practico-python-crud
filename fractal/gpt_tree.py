import turtle
import random

def draw_tree(branch_length, t):
    if branch_length > 5:
        # Dibuja el tronco
        t.pensize(branch_length / 20)
        t.forward(branch_length)

        # Ramificación derecha
        t.right(20)
        draw_tree(branch_length - 15, t)

        # Retrocede y regresa a la posición original
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("sky blue")

    tree_turtle = turtle.Turtle()
    tree_turtle.speed(1)
    tree_turtle.color("brown")
    tree_turtle.pensize(2)

    # Posiciona la tortuga en la base del árbol
    tree_turtle.left(90)
    tree_turtle.up()
    tree_turtle.backward(100)
    tree_turtle.down()

    # Dibuja el árbol
    draw_tree(80, tree_turtle)

    screen.mainloop()

if __name__ == "__main__":
    main()

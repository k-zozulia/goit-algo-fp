import turtle

def draw_pythagoras_tree(branch_length, level):
    if level == 0:
        return
    
    turtle.forward(branch_length)
    turtle.right(30)
    draw_pythagoras_tree(branch_length * 0.7, level - 1)
    turtle.left(60)
    draw_pythagoras_tree(branch_length * 0.7, level - 1)
    turtle.right(30)
    turtle.backward(branch_length)

def setup_turtle():
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(200)
    turtle.down()

def main():
    level = -1
    while level < 0 or level > 10:
        try:
            level = int(input("Введіть рівень рекурсії (від 0 до 10): "))
        except ValueError:
            print("Будь ласка, введіть коректне ціле число.")
    
    setup_turtle()
    draw_pythagoras_tree(150, level)
    
    turtle.done()

if __name__ == "__main__":
    main()
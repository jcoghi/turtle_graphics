from brain import start

print("Welcome to Turtle Drawing")
print('''Select
        D for Dots;
        T for triangle
        S for Square
        P for Spirograph
        R for Turtle Race
        E for Etch-a-Sketch''')

start(input("What do you want to draw? ")).lower()


import drawnings

def start(opcao):
    if opcao == 'd':
        drawnings.dots()
    elif opcao == "t":
        drawnings.triangle()
    elif opcao == 's':
        drawnings.square(float(input("Insert size of side: ")))
    elif opcao == "p":
        drawnings.spirograph()
    elif opcao == 'r':
        drawnings.race()
    elif opcao == 'e':
        drawnings.etch()
    else:
        print("Please, select a valid option.")

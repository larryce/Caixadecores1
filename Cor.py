def adicionarcor(cores):
    cor = str(input("Entre com uma cor:"))
    cores.append(cor)

def listarcores(cores):
    for cor in cores:
        print(cor)
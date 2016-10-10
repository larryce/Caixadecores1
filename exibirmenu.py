import Cor

cores = []

opcao = 0
while opcao != 3:
    print("Digite sua opção: 1 - Adicionar cor, 2- listar cores")
    opcao = int(input("entre com sua opcao:"))
    if(opcao==1):
        Cor.adicionarcor(cores)
    else:
        Cor.listarcores(cores)

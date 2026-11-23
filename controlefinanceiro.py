def main():

    descricoes = []
    valores = []
    tipos = []

    opcao = "0"

    while opcao != "5":

        print("=================================")
        print("     CONTROLE FINANCEIRO PESSOAL")
        print("=================================")
        print()
        print("1 - Adicionar receita")
        print("2 - Adicionar despesa")
        print("3 - Consultar saldo")
        print("4 - Listar movimentacoes")
        print("5 - Sair")
        print()

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            adicionar_movimentacao(
                descricoes, valores, tipos, "receita"
            )

        elif opcao == "2":
            adicionar_movimentacao(
                descricoes, valores, tipos, "despesa"
            )

        elif opcao == "3":
            mostrar_saldo(valores, tipos)

        elif opcao == "4":
            listar_movimentacoes(descricoes, valores, tipos)

        elif opcao == "5":
            print("Programa encerrado!")

        else:
            print("Opcao invalida!")


def adicionar_movimentacao(descricoes, valores, tipos, tipo):

    descricao = input("Digite a descricao: ")
    valor = float(input("Digite o valor: "))

    descricoes.append(descricao)
    valores.append(valor)
    tipos.append(tipo)

    print("Movimentacao cadastrada com sucesso!")



def calcular_saldo(valores, tipos):

    total_receitas = 0
    total_despesas = 0

    for i in range(len(valores)):

        if tipos[i] == "receita":
            total_receitas = total_receitas + valores[i]
        else:
            total_despesas = total_despesas + valores[i]

    saldo = total_receitas - total_despesas

    return saldo



def mostrar_saldo(valores, tipos):

    total_receitas = 0
    total_despesas = 0

    for i in range(len(valores)):

        if tipos[i] == "receita":
            total_receitas = total_receitas + valores[i]
        else:
            total_despesas = total_despesas + valores[i]

    saldo = calcular_saldo(valores, tipos)

    print("\n--- RESUMO FINANCEIRO ---")
    print("Total de receitas: R$", total_receitas)
    print("Total de despesas: R$", total_despesas)
    print("Saldo atual: R$", saldo)



def listar_movimentacoes(descricoes, valores, tipos):

    print("\n--- MOVIMENTACOES ---")

    if len(descricoes) == 0:
        print("Nenhuma movimentacao cadastrada.")

    else:
        for i in range(len(descricoes)):

            print("Descricao:", descricoes[i])
            print("Tipo:", tipos[i])
            print("Valor: R$", valores[i])
            print("--------------------")

main()

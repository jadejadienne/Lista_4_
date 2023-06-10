# Escreva uma função que receba uma lista de dicionários, onde cada dicionário representa
# um aluno com as chaves "nome" e "nota". A função deve retornar o nome do aluno com a maior nota.

def maior_nota_aluno(lista_dicionarios):
    Not_maior = 0
    Nom_alu = " "
    for reecebe in lista_dicionarios:
        Notas = reecebe["Nota"]
        Nomes = reecebe["Nome"]
        if Notas > Not_maior:
            Not_maior = Notas
            Nom_alu = Nomes
    return Nom_alu, Not_maior


def main():
    Alu = []
    Dic = {}

    print("dga-me o nome do aluno e a sua nota que voçê deseja: ")
    for rece in range(0, 3):
        Nom_alu = input("Nome do aluno que voçê deseja: ")
        Num_not = int(input("Nota do aluno que voçê deseja {rece + 1}: "))
        Dic = {"Nome": Nom_alu, "Nota": Num_not}
        Alu.append(Dic)

    print("Lista dos dicionários dos alunos: ")
    print(Alu)

    resposta = maior_nota_aluno(Alu)
    print("O aluno com a maior nota é:", resposta)
        
if __name__ == "__main__":
     main()


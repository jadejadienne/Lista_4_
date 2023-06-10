#Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.


def calculo_da_soma(lista_nueros):
    soma = 0 
    for numero in lista_nueros:
        soma += numero
    return soma

def main():
    
    lista_numeros= []
    
    for num in range(0,5):
        numero = int(input("digite o número que voçê deseja: "))  
        lista_numeros.append(numero)  
           
    R = calculo_da_soma(lista_numeros)
    print("a soma do resultado é: ", R)
          
if __name__ == "__main__":
    main()
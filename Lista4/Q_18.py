#Crie uma função que receba duas listas de números e retorne uma nova lista contendo
# apenas os elementos que estão presentes em ambas as listas.

def elemento_lista(lista_1 , lista2):
    
    lista_principal = []
    
    for elemen in lista_1:
        if elemen in lista2:
            lista_principal.append(elemen)
    return lista_principal 
    
def main():
        
    lista_1 = []
    for n in range(1,6):
        num = int(input("digite o numero que voçê deseja:"))
        lista_1.append(num)
    print("lista 1: ", lista_1)
    
    lista2 = []
    
    for n in range(1,6):
        num = int(input("digite o numero que voçê deseja:"))
        lista2.append(num)
    print("lista 2: ", lista2)
    
   
if __name__ == "__main__":
    main()
    

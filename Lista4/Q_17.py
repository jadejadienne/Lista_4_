#Implemente uma função que receba uma lista de strings 
# e retorne uma nova lista contendo apenas as strings que possuem mais de 5 caracteres.



def caracteres(lista_strings):
    list_N  = []
    
    for pal in lista_strings:
        if len(pal) >= 5:
            list_N.append(pal)
    return list_N

def main():
    
    list_palavra = []
     
    for Rec in range(0,3):
        p = input("digite a palvra que vc deseja: ")
        list_palavra.append(p)
    R = caracteres (list_palavra)    
    print("5 caracteres", R)     
               
if __name__ == "__main__":
     main()
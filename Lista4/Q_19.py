#Implemente uma função que receba uma lista de palavras e retorne a palavra mais longa presente na lista.

def palavra_longa(lista_palavras):
    pala_l = " "
    
    for pal in lista_palavras:
        if len(pal) > len(pala_l):
            pala_l = pal
    return pala_l

def main():
    
    l_palavras = []
    
    for recebe in range(1,6):
        p = input("digite a palavra que voçê deseja: ")
        l_palavras.append(p)
        
    res = palavra_longa(l_palavras) 
    print("palavra mais longa ", res)
 
 
if __name__ == "__main__":
    main()
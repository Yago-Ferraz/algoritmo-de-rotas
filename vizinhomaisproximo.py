def main():
    pontos = arquivos()
    menor_caminho = caminho(pontos)
    melhor_caminhostr = string(menor_caminho)
    return melhor_caminhostr

def arquivos():

    nome_do_arquivo=input('digite o nome do arquvio: ')
    f = open(f'{nome_do_arquivo}.txt','r')
    a = f.readlines()
    tamanho_matriz=(int(a[0][0]),int(a[0][2]))
    a.pop(0)
    for k in range(0,tamanho_matriz[0]):
        a[k]=a[k].replace('\n','')
        a[k]=a[k].split()

        pontos=[]
        for k in range(0,len(a)):
            for i in range(0,len(a[k])):
                try:
                    i = int(a[k][i])
                except:
                    if a[k][i] !='R':
                        pontos.append(([k,i],a[k][i]))


    return pontos


def distancia(ponto_atual,ponto_objetivo):
    return abs(abs(ponto_atual[0]-ponto_objetivo[0])+ abs(ponto_atual[1]-ponto_objetivo[1]))



def caminho(matriz):
    no_atual = None
    no_atual = matriz[0]
    matriz.pop(0)
            
    caminho=[no_atual[1]]
    while len(matriz)>0:
        menor_distancia = float('inf')
        for k in range(0,len(matriz)):
            no_proximo = matriz[k]
            dist = distancia(no_atual[0],no_proximo[0])
            if dist <menor_distancia:
                menor_distancia=dist
                prox = matriz[k]
                apagar= k
        
        no_atual = prox
        caminho.append(no_atual[1])
        matriz.pop(apagar)
    return caminho
        
def string(caminho):
    melhor_caminho = ''
    for k in caminho: 
        melhor_caminho = melhor_caminho + " "+ k

    return melhor_caminho

print(main())
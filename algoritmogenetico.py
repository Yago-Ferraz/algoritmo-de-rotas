import random
def main(n):
    dicionario = arquivos()
    populacoa = populacaoInicial(n,dicionario,list(dicionario.keys()))
    select = selecao(populacoa)
    nova_populacao=reproducao(n,select,dicionario)
    melhor_anterior = melhorIndividuo(nova_populacao)
    melhorvezes =0
    while melhorvezes <3:
        select = selecao(nova_populacao)
        nova_populacao=reproducao(n,select,dicionario)
        melhor = melhorIndividuo(nova_populacao)
        if melhor[len(melhor)-1]==melhor_anterior[len(melhor_anterior)-1]:
            melhorvezes=melhorvezes+1
            melhor_anterior = melhor
        else:
            melhor_anterior = melhor
            melhorvezes=0
    melhor_str= string(melhor[0:len(melhor)-1])
    print(melhor[-1])
    return melhor_str

def melhorIndividuo(populacao):
    melhor = float('inf')
    melhor_ponto=None
    for k in populacao:
        if k[len(k)-1] <melhor:
            melhor=k[len(k)-1]
            melhor_ponto=k
    return melhor_ponto


def arquivos():

    nome_do_arquivo=input('digite o nome do arquvio: ')
    f = open(f'{nome_do_arquivo}.txt','r')
    a = f.readlines()
    tamanho_matriz=(int(a[0][0]),int(a[0][2]))
    a.pop(0)
    for k in range(0,tamanho_matriz[0]):
        a[k]=a[k].replace('\n','')
        a[k]=a[k].split()

        pontos={}
        for k in range(0,len(a)):
            for i in range(0,len(a[k])):
                try:
                    i = int(a[k][i])
                except:
                    
                    if a[k][i] !='R':
                        pontos[a[k][i]]=[k,i]

    return pontos

def distancia(ponto_atual,ponto_objetivo):
    return abs(abs(ponto_atual[0]-ponto_objetivo[0])+ abs(ponto_atual[1]-ponto_objetivo[1]))


def fitness(individo,dicionario):
    distancia_percorrida=0
    for k in range(1,len(individo)-1):
        distancia_percorrida = distancia_percorrida + distancia(dicionario[individo[k-1]],dicionario[individo[k]])
    individo[len(individo)-1]=distancia_percorrida

def populacaoInicial(n,dicionario,genes,populacao = []):
    while len(populacao)<n:
        individuo = criarIdividuo(genes)
        fitness(individuo,dicionario)
        populacao.append(individuo)
    return populacao

def criarIdividuo(genes):
    g = [i for i in genes ]
    individuo = []
    for k in range(len(genes)):
        gene = random.randrange(0,len(g))
        individuo.append(g[gene])
        g.pop(gene)
    individuo.append(0)
    return individuo

def selecao(populacao):
    melhores=[]
    media=0
    for k in populacao:
        media = media + k[len(k)-1]
    media=media/len(populacao)
    k=0
    while k<=len(populacao)-1:
        if populacao[k][len(populacao[k])-1]<media:
            melhores.append(populacao[k])
            populacao.pop(k)
        k=k+1
    while (len(melhores))<len(populacao)/2:
        melhores.append(populacao[0])
        populacao.pop(0)
    
    return melhores

def reproducao(n,melhores,dicionario):
    while len(melhores)<n:
        pai= random.randrange(0,len(melhores)-1)
        filho =filhos(melhores[pai])
        fitness(filho,dicionario)
        melhores.append(filho)
    return melhores
def ismutado():
    n= random.randrange(0,100)
    if n ==1:
        return True
    return False

def filhos(individuo):
    filho = [i for i in individuo]
    genea = random.randrange(0,len(individuo)-2)
    geneb = random.randrange(0,len(individuo)-2)
    filho[genea],filho[geneb]=filho[geneb],filho[genea]
    if ismutado():
        a = random.randrange(0,len(individuo)-2)
        b = random.randrange(0,len(individuo)-2)
        filho[a],filho[b]=filho[b],filho[a]

    
    return filho
    

def string(caminho):
    melhor_caminho = ''
    for k in caminho: 
        melhor_caminho = melhor_caminho + " "+ k
       
    return melhor_caminho

print(main(100))
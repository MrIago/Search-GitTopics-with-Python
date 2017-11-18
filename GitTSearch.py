# APLICANDO NO SITE DO GITHUB

# RECOMENDO ABRIR COM A IDLE DO PYTHON, POIS SÃO MUITOS PROJETOS,
# ENTÃO PELO CMD ACABA SUMINDO OS PRIMEIROS PROJETOS

# OBETER UM LISTA DE LINKS DE UM TÓPICO QUALQUER

# 1º PRECSAMOS OBTER O HTML COM O MODULO REQUESTS

import requests

from bs4 import BeautifulSoup

def mostra_topico(topico):

    # cria um lista onde será guardado os links
    desc = []

    # agora pega o html da pagina do topico
    r = requests.get('https://github.com/topics/%s' %(topico))

    print('Status do Pedido: %i = %s\n\n' %(r.status_code, 'OK' if r.status_code == 200 else 'ERRO'))

    # fazer o parser para interpretar o html
    s = BeautifulSoup(r.content,  "html.parser")

    # agora é só procurar os titulos na pagina

    n = 0 # contador para os titulos

    print("Projetos no Topico %s:\n\n" %(topico))
    
    
    for a in s.findAll('div', attrs={'class':'text-gray mb-3 ws-normal'}):

        desc.append(a.text)

    for a in s.findAll('h3', attrs={'class': 'f3'}):
        
        print()
        
        print('.'*77)

        print('\nProject', n, ':\n')
        print(a.text)

        try:
            print(desc[n])

        except:
            print("ERRO DE CODIFICAÇÃO")
            
        print()

        print('.'*77)

        print()

        n += 1

# Pronto, agora é só chamar a função

topic = input("Topico: ").lower()

mostra_topico(topic)

import os

os.system('pause')

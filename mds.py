import cv2
import numpy as np
import PIL
from PIL import Image

cmd_igual = "="
cmd_print= "print"
cmd_input= "input"
cmd_if = "if"
cmd_else = "else"

lista_imagens_if = []
def img_final(lista_imagens):
    imgs    = [ PIL.Image.open(i) for i in lista_imagens ]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

    # save that beautiful picture
    imgs_comb = PIL.Image.fromarray( imgs_comb)
    imgs_comb.save( 'Trifecta.jpg' )    

    # for a vertical stacking it is simple: use vstack
    imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = PIL.Image.fromarray( imgs_comb)
    imgs_comb.save( 'Trifecta_vertical.jpg' )

def img_input(i,lista_imagens,linha):
    pos_input =  linha.find(cmd_input)
    nome = linha[0:pos_input-3]
    imagem = cv2.imread('input.jpg')
    nome_imagem = 'img'+str(i)+'.png'
    #Texto
    #cv2.putText(imagem, ‘Texto’, (coluna_inicial, linha_inicial), fonte, expessura, cor, tipo de linha)
    cv2.putText(imagem, nome, (400,130),cv2.FONT_HERSHEY_SIMPLEX , 1, (80, 80, 80), cv2.LINE_4)
    cv2.imwrite(nome_imagem,imagem)
    #cv2.imshow(nome_imagem, imagem)
    lista_imagens.append(nome_imagem)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows() 


def img_if(i,lista_imagens,linha):
    pos_if =  linha.find(cmd_if)
    tamanho = len(linha)
    condicao = linha[pos_if+2:tamanho-2]
    
    imagem = cv2.imread('branco.png')
    cv2.imwrite('condicao1.png',imagem)
    lista_imagens_if.append('condicao1.png')

    imagem = cv2.imread('if.png')
    nome_imagem = 'img'+str(i)+'.png'
    #Texto
    #cv2.putText(imagem, ‘Texto’, (coluna_inicial, linha_inicial), fonte, expessura, cor, tipo de linha)
    cv2.putText(imagem, condicao, (350,165),cv2.FONT_HERSHEY_SIMPLEX , 1, (80, 80, 80), cv2.LINE_4)
    cv2.imwrite(nome_imagem,imagem)
    #cv2.imshow(nome_imagem, imagem)
    lista_imagens.append(nome_imagem)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def img_else(i,lista_imagens):
    imagem = cv2.imread('else.png')
    print(lista_imagens_if)
    imgs    = [ PIL.Image.open(i) for i in lista_imagens_if ]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

    # save that beautiful picture
    imgs_comb = PIL.Image.fromarray( imgs_comb)
    imgs_comb.save( 'condicaoIF.jpg' )    
    lista_imagens.append('condicaoIF.jpg')
    '''
    # for a vertical stacking it is simple: use vstack
    imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = PIL.Image.fromarray( imgs_comb)
    imgs_comb.save( 'Trifecta_vertical.jpg' )
    '''
    nome_imagem = 'img'+str(i)+'.png'
    cv2.imwrite(nome_imagem,imagem)
    #cv2.imshow(nome_imagem, imagem)
    lista_imagens.append(nome_imagem)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def img_print(i,lista_imagens, linha, condicao_if):
    tamanho = len(linha)
    pos_print =  linha.find(cmd_print)
    frase = linha[pos_print+7:tamanho-3]
    imagem = cv2.imread('print.png')
    nome_imagem = 'img'+str(i)+'.png'
    #Texto
    #cv2.putText(imagem, ‘Texto’, (coluna_inicial, linha_inicial), fonte, expessura, cor, tipo de linha)
    cv2.putText(imagem, frase, (100,180),cv2.FONT_HERSHEY_SIMPLEX , 1, (80, 80, 80), cv2.LINE_4)
    cv2.imwrite(nome_imagem,imagem)
    #cv2.imshow(nome_imagem, imagem)
    if(condicao_if == True):
        lista_imagens_if.append(nome_imagem)
    else:
        lista_imagens.append(nome_imagem)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows() 

def img_atribuicao(i,lista_imagens, linha):
    tamanho = len(linha)
    pos_igual = linha.find(cmd_igual)
    nome = linha[0:pos_igual]
    conteudo = linha[pos_igual+1:tamanho-1]
    imagem = cv2.imread('atribuicao.png')
    nome_imagem = 'img'+str(i)+'.png'
    #Texto
    #cv2.putText(imagem, ‘Texto’, (coluna_inicial, linha_inicial), fonte, expessura, cor, tipo de linha)
    cv2.putText( imagem, conteudo, (466,144), cv2.FONT_HERSHEY_SIMPLEX , 1, (80, 80, 80), cv2.LINE_4)
    cv2.putText(imagem, nome, (200,417), cv2.FONT_HERSHEY_SIMPLEX , 1, (80, 80, 80), cv2.LINE_4)
    cv2.imwrite(nome_imagem,imagem)
    #cv2.imshow(nome_imagem, imagem)
    lista_imagens.append(nome_imagem)
    

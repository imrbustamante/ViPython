#Usar
#python 01_desenho_e_texto_em_imagem.py

#Biblioteca
import mds

########################################################################

#abrindo o arquivo
nome_arquivo = input("digite o nome  do arquivo.py: ")
lista_imagens = []
i = 0
condicao_if = False
with open(nome_arquivo) as file:
    for linha in file:       
        if linha != '':
            i += 1 
            if linha.find(mds.cmd_print) != -1:   
                mds.img_print(i,lista_imagens, linha, condicao_if)
            elif linha.find(mds.cmd_input) != -1:
                mds.img_input(i,lista_imagens, linha)
            elif linha.find(mds.cmd_if) != -1:
                condicao_if = True
                mds.img_if(i,lista_imagens, linha)
            elif linha.find(mds.cmd_else) != -1:
                condicao_if = False
                mds.img_else(i,lista_imagens)
            elif linha.find(mds.cmd_igual) != -1:
                mds.img_atribuicao(i,lista_imagens, linha)
print("Fim do arquivo")

print(lista_imagens)
mds.img_final(lista_imagens)

#Referencia
#https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html

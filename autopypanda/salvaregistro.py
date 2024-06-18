import pandas as pd
from PIL import Image, ImageDraw, ImageFont

image = Image.open('./certificado_padrao.jpg')
desenhar = ImageDraw.Draw(image)
fonte_nome = ImageFont.truetype('./tahomabd.ttf', 90)
fonte_geral = ImageFont.truetype('./tahoma.ttf', 80)
fonte_data = ImageFont.truetype('./tahoma.ttf', 55)

# Carregar os dados da planilha
planilha_alunos = pd.read_excel('planilha_alunos.xlsx', sheet_name='Sheet1')

for index, coluna in planilha_alunos.iterrows():
    nome_curso = coluna.iloc[0]
    nome_participante = coluna.iloc[1]
    tipo_participacao = coluna.iloc[2]
    data_inicio = coluna.iloc[3]
    data_termino = coluna.iloc[4]
    carga_horaria = coluna.iloc[5]
    data_emissao = coluna.iloc[6]
    
    image = Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(image)
    desenhar.text((1020, 825), nome_participante, fill='black',font=fonte_nome)
    desenhar.text((1070, 950), nome_curso, fill='black', font=fonte_geral)
    desenhar.text((1430, 1070), tipo_participacao, fill='black', font=fonte_geral)
    desenhar.text((1480, 1180), str(carga_horaria), fill='black', font=fonte_geral)
    desenhar.text((750, 1770), data_inicio, fill='blue', font=fonte_data)
    desenhar.text((750, 1930), data_termino, fill='blue', font=fonte_data)
    desenhar.text((2220, 1930), data_emissao, fill='black', font=fonte_data)
    image.save(f'./{index} {nome_participante} certificado.png')
from PIL import  Image, ImageDraw, ImageFont
from datetime import datetime
import os

image_path = os.path.join(os.getcwd(),'imagens')

# Carregando a imagem a ser cortada
img = Image.open(os.path.join(image_path,"cotacao.png"))

# Definindo as coordenadas do retângulo a ser cortado
left = 1
upper = 1
right = img.width
lower = img.height

# Cortando a imagem
img_cropped = img.crop((left, upper, right, lower))

# Salvando a imagem cortada
img_cropped.save('.\imagens\cotacao.png')

# Carregando as imagens de fundo e tabela
background = Image.open(os.path.join(image_path,"background.jpg"))
table = Image.open(os.path.join(image_path,"cotacao.png"))

# Calculando as novas dimensões da imagem
width, height = table.size
new_width = int(width * 1.8)
new_height = int(height * 1.8)

# Aumentando a imagem
table = table.resize((new_width, new_height))

# Colocando a tabela sobre o fundo
background.paste(table, (140,900))


# Iniciando o objeto para desenhar na imagem
draw = ImageDraw.Draw(background)

# Selecionando a fonte
font = ImageFont.truetype("arial.ttf", 24)

# Pegando a data atual
current_date = datetime.now()

# Formatando a data no formato desejado
formatted_date = current_date.strftime("%d/%m/%Y")

# Adicionando textos na imagem

draw.text((500, 750), formatted_date, fill=(38, 45, 46), font=font)
draw.text((500, 1200), "Fonte: B3", fill=(38, 45, 46), font=font)

# Salvando a imagem final

background.save("Mercado_Futuro_Boi.png")


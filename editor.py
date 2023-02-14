from PIL import  Image, ImageDraw, ImageFont
from datetime import datetime
import os

def edit_image(image_path,background_img,boi_milho):
    # Carregando a imagem a ser cortada
    img = Image.open(image_path)

    # Definindo as coordenadas do retângulo a ser cortado
    left = 1
    upper = 1
    right = img.width
    lower = img.height

    # Cortando a imagem
    img_cropped = img.crop((left, upper, right, lower))

    # Salvando a imagem cortada
    img_cropped.save(os.path.join(os.path.dirname(image_path), f"cotacao_{boi_milho}.png"))

    # Carregando as imagens de fundo e tabela
    background = Image.open(os.path.join(os.path.dirname(image_path), background_img))
    table = Image.open(os.path.join(os.path.dirname(image_path), f"cotacao_{boi_milho}.png"))
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
    fixed_date = formatted_date.replace('/','-')

    # Adicionando textos na imagem

    draw.text((500, 750), formatted_date, fill=(38, 45, 46), font=font)
    draw.text((500, 1200), "Fonte: B3", fill=(38, 45, 46), font=font)

    # Salvando a imagem final
    folder_path = os.path.join(os.getcwd(),'cotacao_mercado_futuro')
    output_path = os.path.join(folder_path, f"Mercado_Futuro_{boi_milho}_{fixed_date}.png")
    background.save(output_path)
    
    return Image.open(output_path)

image_path = os.path.join(os.getcwd(),'imagens')

# Carregando a imagem a ser cortada
img = os.path.join(image_path,"cotacao_boi.png")
background_img = os.path.join(image_path,"background_boi.jpg")
img2 = os.path.join(image_path,"cotacao_milho.png")
background2_img = os.path.join(image_path,"background_milho.jpg")

boi_futuro = edit_image(img,background_img,"boi")
milho_futuro = edit_image(img2,background2_img,"milho")
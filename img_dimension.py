import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('Imagem_colada.png')
img_gray = img.convert("L")
img_gray.save("image_converted_gray.jpg")

limiar = 128
img_black_white = img_gray.point(lambda x: 255 if x > limiar else 0, '1')

img_black_white.save("image_converted_black_white.jpg")

print("Imagens salvas com sucesso!")

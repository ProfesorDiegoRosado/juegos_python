# Autor: Profe
# Descripcion: Meme Generator

from PIL import Image, ImageDraw, ImageFont
import sys

image_name = sys.argv[1]
upper_text = sys.argv[2]
lower_text = sys.argv[3]

image = Image.open(image_name)
draw_image = ImageDraw.Draw(image)
myFont = ImageFont.truetype('Breakfast.ttf', 80)
draw_image.text((28, 36), upper_text, fill=(255, 255, 255), font=myFont)
draw_image.text((400, 400), lower_text, fill=(255, 255, 255), font=myFont)
image.show()
image.save("meme.jpg")

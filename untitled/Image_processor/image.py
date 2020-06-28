from PIL import Image, ImageFilter

img = Image.open('./Pokedex/original (1).jpg')
print(img.size)
img.thumbnail((40,40))
print(img.size)
img.save("blur.png","png")
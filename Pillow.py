from PIL import Image

img = Image.open("guy.jpg")
print(img.size)
print(img.format)
img.show()

from PIL import Image

img = Image.open("guy.jpg")
are = (100, 100, 300, 375)
cropped_img = img.crop()

img.show()
cropped_img.show()

# Combine Images Together
sister = Image.open("sister.jpg")
girl = Image.open("girl.jpg")
are = (100, 100, 300, 375)
sister.paste(girl, are)
sister.show()

# Getting Individual Channels
sister = Image.open("sister.jpg")
r, g, b = sister.split()
r.show()
g.show()
b.show()

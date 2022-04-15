from PIL import Image, ImageFilter

before = Image.open("vase.JPG")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out2.bmp")
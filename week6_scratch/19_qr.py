import os
import qrcode

img = qrcode.make("https://youtu.be/xvFZjo5PgG0")

img.save("qr.png", "PNG")

#os.system("open qr.png") #open wasn't working, but the program did successfully output a qr.png
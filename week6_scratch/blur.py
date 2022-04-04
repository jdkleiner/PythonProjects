from PIL import Image, ImageFilter
#Library: Image
#Function: open
#Argument: bridge.bmp
#Variable: before (this is an object, inside of which is a function called filter, which takes
# an argument (ImageFilter.BoxBlur(10)), which itself is a function that just returns the filter to use)
#.save: just saves the file for you
before = Image.open("vase.JPG")
after = before.filter(ImageFilter.BoxBlur(10)) #10 is the number of pixels around which to blur
after.save("out.JPG")
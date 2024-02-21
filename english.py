#Anything easy like history or reading, convert img to txt, gpt, make sure to ask it to explain its response, then cut the response to only the needed answer choice

import pytesseract as tess
import re
import PIL

img = PIL.Image.open('Screen-Shot-2021-04-26-at-7.53.58-PM.png')
pix = img.load()
print(img.mode)
w, h = img.size

# for y in range(h):
#   for x in range(w):
#     r = pix[x,y][0]
#     g = pix[x,y][1]
#     b = pix[x,y][2]
#     a = pix[x,y][3]
#     pix[x,y] = (r, g, b, a)
#     if pix[x,y] != (255, 255, 255, a):
#       pix[x,y] = (0, 0, 0, a)

# img.save('test1.png')

print(tess.image_to_string(img))
print("Done")
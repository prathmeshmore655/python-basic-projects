import qrcode

img=qrcode.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=1")

qrcode.make_image(fill_color="red",back_color="blue")
img.save("img.png")
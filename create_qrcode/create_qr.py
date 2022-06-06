import pyqrcode

data =str(input("Enter the website link : "))

img = pyqrcode.create(data)

img.png('webiste.png', scale= 10)
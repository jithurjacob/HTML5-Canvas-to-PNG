from binascii import a2b_base64

data = open("data.txt").read().replace("data:image/png;base64,", "")
binary_data = a2b_base64(data)

fd = open('image.png', 'wb')
fd.write(binary_data)
fd.close()
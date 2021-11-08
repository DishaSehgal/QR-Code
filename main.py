import qrcode

#The version attribute determines the matrix size of the QR code.
# The error correction used for the QR Code scan is analyzed with the error connection attribute.
# The box size is the pixel size of each box
# the border controls the thickness.
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
#create a variable to store the info,
data="https://github.com/DishaSehgal"
#data="Hello! Welcome to the world of programming"

#encode the link
img=qrcode.make(data)
print(type(img))

#save the qr code
img.save("Disha github qrcode.jpg")

import cv2

#create the decoder
decoder=cv2.QRCodeDetector()

#load your data
file_name="Disha github qrcode.jpg"
image=cv2.imread(file_name)

#decode and print the required info
link, data_points,straight_qrcode=decoder.detectAndDecode(image)
print(link)





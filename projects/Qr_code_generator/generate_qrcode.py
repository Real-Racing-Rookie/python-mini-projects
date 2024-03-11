import qrcode
import sys

try:
    input_URL = sys.argv[2]
except:
    input_URL = input("whats the url?")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("url_qrcode.png")

print(qr.data_list)

import qrcode
url = input("ENTER YOU URL: ").split()
file_path = "C:\\Users\\HP\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR code was generated")
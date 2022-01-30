import qrcode

class QRCode:
    def createQR(self,s : str, fileName : str, output : str, type : str):
        qr = qrcode.QRCode()
        qr.add_data(s)
        qr.make()
        img = qr.make_image()
        img.save(f"{output}/{fileName}.{type}")






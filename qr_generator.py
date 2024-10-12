import qrcode
from datetime import datetime

def generator(name,ex_date,file_name):
	qr_date = f"{name},{ex_date.strftime('%Y-%m-%d')}"

	# Generates a empty QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box (pixel size)
        border=4,  # Border thickness
    )

    qr.add_data(qr_date)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    img.save(file_name)
	print(f"QR Code generated for {name} with expiry {ex_date.strftime('%Y-%m-%d')}")

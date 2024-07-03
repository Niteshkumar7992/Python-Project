# import qrcode
# # Taking upi id as a amount
# upi_id = input("Enter your upi id = ")
# # upi://pay?pa=upi_?ID&pn=ID

# phonepe_url =f'upi://pay?pa={upi_id}&pn=Recipient%20NName&mc = 1234'
# paytm_url =f'upi://pay?pa={upi_id}&pn=Recipient%20NName&mc = 1234'
# google_pay_url =f'upi://pay?pa={upi_id}&pn=Recipient%20NName&mc = 1234'

# phonepe_qr = qrcode.make(phonepe_url)
# paytm_qr = qrcode.make(paytm_url)
# google_pay_url_qr = qrcode.make(google_pay_url)
# # save the QR code to image file (optional)
# phonepe_qr.save('phonepe_qr.png')
# paytm_qr.save('paytm_qr.png')
# google_pay_qr.save('google_pay_qr.png')

# # Display the QR codes (you may need to install  pIL/Pillow Library)
# phonepe_qr.show()
# paytm_qr.show()
# google_pay_qr.show()




import qrcode
from PIL import Image

# Taking UPI ID as input
upi_id = input("Enter your UPI ID: ")

# URLs for UPI payment apps
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Generating QR codes
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Saving QR codes to image files
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Displaying the QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

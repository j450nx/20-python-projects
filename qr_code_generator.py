# install all the libraries needed
# pip3 install qrcode Image
# create a function that collects a text and converts it to a qrcode
# save the qrcode as an image
# run the function
import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 20,
        border = 0
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('qrcode.png')


url = input('Enter your url: ')
generate_qrcode(url)
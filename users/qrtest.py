import png, os
import random, string

import qrcode.image.svg
def qr_maker(value, registration_id):
    factory = qrcode.image.svg.SvgPathFillImage
    svg_img=qrcode.make(f"value", image_factory=factory)
    return(svg_img.save(f"{registration_id}.svg"))



def generate_user_secure_id():
        return ''.join(random.choices(string.ascii_uppercase +
                            string.digits, k=8))
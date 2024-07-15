import qrcode
import random
import string
import logging

logger = logging.getLogger(__name__)

def generate_user_secure_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def qr_maker(value, registration_id):
    logger.info(f"{registration_id}")
    factory = qrcode.image.svg.SvgPathFillImage
    svg_img = qrcode.make(value, image_factory=factory)
    file_path = f"{registration_id}.svg"
    logger.info(f"Saving QR code to file: {file_path}")
    svg_img.save(file_path)
    return file_path
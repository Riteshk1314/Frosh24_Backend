import qrcode
import random
import string
import logging
from django.core.mail import get_connection, EmailMessage
from django.core.mail import send_mail
from django.conf import settings

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


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_credentials_email(email, registration_id, password):
    subject = 'Your Account Credentials'
    message = f"""
    Greetings from Frosh 2024! 

    Here are your credentials for booking tickets of frosh events:

    Registration ID: your registration ID 
    Password: {password}

    Please log in to the https://froshtiet.com/ to book your tickets.
    

    Best regards,
    Frosh 2024
    
    """
    
    msg = MIMEMultipart()
    msg['From'] = settings.DEFAULT_FROM_EMAIL
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = None
    try:
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.connect(settings.EMAIL_HOST, settings.EMAIL_PORT)  # Explicitly call connect
        server.ehlo()
        if settings.EMAIL_USE_TLS:
            server.starttls()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.send_message(msg)
        logger.info(f"Credentials email sent to {email}")
    except Exception as e:
        logger.error(f"Failed to send credentials email to {email}: {str(e)}")
        logger.exception("Detailed traceback:")
        raise
    finally:
        if server:
            try:
                server.quit()
            except Exception:
                pass
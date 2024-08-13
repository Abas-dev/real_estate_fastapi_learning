from passlib.context import CryptContext
from fastapi import BackgroundTasks
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from config import get_settings
from typing import List
import pyotp

settings = get_settings()

conf = ConnectionConfig(
    MAIL_USERNAME = f"{settings.MAIL_USERNAME}",
    MAIL_PASSWORD = f"{settings.MAIL_PASSWORD}",
    MAIL_FROM = f"{settings.MAIL_FROM}",
    MAIL_PORT = f"{settings.MAIL_PORT}",
    MAIL_SERVER = f"{settings.MAIL_SERVER}",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

pwd_context = CryptContext(schemes=['bcrypt'])


def send_email(bg_task: BackgroundTasks, message: str, recipient: List, subject: str):
    email_message = MessageSchema(
        subject = subject,
        recipient = recipient,
        body = message,
        sub_type = "html"
    )

    fm = FastMail(conf)
    BackgroundTasks.add_task(fm.send_message, email_message)

def hash_password(password: str):
    return pwd_context.hash(password)
    
def verify_password(rw_password: str, hashed_password: str):
    return pwd_context.verify(rw_password, hashed_password)

secret = pyotp.random_base32()
time_otp = pyotp.TOTP(secret, interval=180)

def generate_otp():
    otp = time_otp.now()
    return otp

def verify_otp(code): 
    verify = time_otp.verify(code)
    return verify

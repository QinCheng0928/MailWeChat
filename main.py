import imaplib
import email
from email.header import decode_header
import requests
import os

IMAP_SERVER = os.environ.get("IMAP_SERVER")
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
SC_KEY = os.environ.get("SC_KEY")

def send_wechat(subject, sender):
    url = f"https://sctapi.ftqq.com/{SC_KEY}.send"
    data = f"邮件: {subject}, 发件人: {sender}"
    print(f"send data: {data}")
    requests.post(url, data=data)

def check_mail():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("INBOX")

        _, response = mail.search(None, 'UNSEEN')
        mail_ids = response[0].split()
        print(f"mail_ids: {mail_ids}")

        if mail_ids:
            for m_id in mail_ids:
                _, msg_data = mail.fetch(m_id, '(BODY.PEEK[])')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject, encoding = decode_header(msg["Subject"])[0]
                        if isinstance(subject, bytes):
                            subject = subject.decode(encoding or "utf-8")
                        sender = msg.get("From")
                        send_wechat(subject, sender)
        mail.logout()
    except Exception as e:
        print(f"fetch error: {e}")

if __name__ == "__main__":
    check_mail()
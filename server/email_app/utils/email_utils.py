from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
from django.template.loader import render_to_string
import os

def send_candidate_email(data, image):
    subject = f"Python Backend Engineer Selection Task - {data['name']}"
    from_email = os.getenv('EMAIL_HOST_USER')
    to_emails = data['recipients']

    html_content = render_to_string("email_template.html", data)
    msg = EmailMultiAlternatives(subject, '', from_email, to_emails)
    msg.attach_alternative(html_content, "text/html")

    img = MIMEImage(image.read())
    img.add_header('Content-ID', '<screenshot>')
    img.add_header('Content-Disposition', 'inline', filename='screenshot.jpg')
    msg.attach(img)

    msg.send()

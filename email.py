import logging

# Sending Email
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)


def send(to, subject, html_body, text_body=None, attachments=None, from_email=None, cc=None):
    if not(isinstance(to, list) or isinstance(to, tuple)):
        to = [to]

    if text_body is None:
        text_body = strip_tags(html_body)

    if cc and not(isinstance(cc, list) or isinstance(cc, tuple)):
        cc = [cc]

    try:
        msg = EmailMultiAlternatives(subject, text_body, to=to)
        if cc:
            msg.cc = cc

        if from_email:
            msg.from_email = from_email

        msg.attach_alternative(html_body, "text/html")
        if attachments is not None:
            for attachment in attachments:
                if attachment:
                    msg.attach(attachment.name, attachment.read())
        msg.send()
        return True
    except:
        logger.exception("Unable to send the mail.")
        return False

def send_from_template(to, subject, template, context, attachments=None, from_email=None, cc=None):
    html_body = render_to_string(template, context)
    return send(to, subject, html_body, attachments=attachments, from_email=from_email, cc=cc)


from project.utils import email

def sendwith_attachment(self):
    
    subject = ""
    send_to = ['example@domin.com', ]
    text_content = """ body we need to write"""
    # add key and values if want to send to template
    dictionary = {'kay1': 'value1'}
    template_name = 'example.html'
    try:
        email.send_from_template(subject=subject, template=template_name, context=dictionary,
                                 to=send_to, attachments=[self.policy_page1, self.policy_page2, self.policy_page3])
        except:
            logger.exception("Unable to send the mail.")

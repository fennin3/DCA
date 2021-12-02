from django.core.mail import send_mail


def sending_mail(message,subject):
    send_mail(
        subject=subject,
        message=message,
        from_email= 'datacareanalyticsorg@gmail.com',
        recipient_list=["enninfrancis47@gmail.com", "kojo.akrasiennin@gmail.com"],
        fail_silently=False,
    )

# def send_sms(message):
#     client = rest.Client(cd.account_sid, cd.auth_token)

#     my_msg = message

#     message = client.messages.create(to=cd.my_cell, from_=cd.my_twilio,  body=my_msg)
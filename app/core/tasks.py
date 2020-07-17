from celery import shared_task
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@shared_task
def send_reg_email(user_pk, domain, to_email):
    mail_subject = 'Activate your account.'
    user = UserModel._default_manager.get(pk=user_pk)
    message = render_to_string('core/acc_active_email.html', {
        'user': user,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()

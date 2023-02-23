from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


def send_confirmation_code(username, email):
    user = get_object_or_404(User, email=email, username=username)
    confirmation_code = default_token_generator.make_token(user)
    user.confirmation_code = confirmation_code
    MESSAGE = (
        f'Здравствуйте, {username}!'
        f'Ваш код подтверждения: {user.confirmation_code}'
    )
    send_mail(
        message=MESSAGE,
        subject='Confirmation code',
        recipient_list=[user.email],
        from_email=settings.DEFAULT_FROM_EMAIL,
    )
    user.save()


# def send_confirmation_code(email, confirmation_code):
#     """Oтправляет на почту пользователя код подтверждения."""
#     send_mail(
#         subject='Код подтверждения',
#         message=f'Ваш код подтверждения: {confirmation_code}',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         recipient_list=(email,),
#         fail_silently=False,
#     )
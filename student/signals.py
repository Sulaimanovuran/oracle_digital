from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save


from config.settings import EMAIL_HOST_USER
from .models import Student


def send_register_mail(email, full_name):
    send_mail(
        "Добро пожаловать",
        f"Здравствуйте {full_name.title()}.\n Рады вам сообщить что вы успешно зарегестрированы в портале нашей школы",
        EMAIL_HOST_USER,
        [email]
    )



@receiver(post_save, sender=Student)
def post_save_student(created, **kwargs):
    instance = kwargs['instance']
    if created:
        send_register_mail(instance.email, instance.full_name)
    else:
        pass


def send_spam_mail(email, full_name, text):
    send_mail(
        f"Здравствуйте {full_name.title()}",
        text,
        EMAIL_HOST_USER,
        [email]
    )
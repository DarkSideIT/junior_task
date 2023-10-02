from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from robots.models import Robot


@receiver(post_save, sender=Robot)
def notify_available_robot(sender, instance, created, **kwargs):
    if instance.is_available:
        subject = f"Робот модели {instance.model}, версии {instance.version} теперь в наличии"
        message = f"Добрый день!\nНедавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."
        from_email = 'tsydypov.ilya@mail.ru'
        recipient_list = ['ilya.tsydypov@gmail.com']  # Замените на нужную вам электронную почту
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
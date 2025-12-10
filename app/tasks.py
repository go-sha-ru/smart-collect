import time

from celery import shared_task

from .models import Payout


@shared_task
def payout_task(payout_id: int):
    """Заадча меняюща статус и тип валюты"""

    time.sleep(8)
    payout = Payout.objects.filter(id=payout_id).first()
    if payout := Payout.objects.filter(id=payout_id).first():
        payout.status = Payout.StatusChoice.APPROVED
        payout.currency = Payout.CurrencyChoice.USD
        payout.save()

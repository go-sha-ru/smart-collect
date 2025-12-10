from django.db import models


class Payout(models.Model):
    """Модель заявки на выплату"""

    class CurrencyChoice(models.IntegerChoices):
        RUB = 643, "RUB"
        USD = 840, "USD"
        EUR = 978, "EUR"

    class StatusChoice(models.IntegerChoices):
        OPENED = 1, "OPENED"
        APPROVED = 2, "APPROVED"

    payment = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="сумма выплаты"
    )
    currency = models.IntegerField(
        choices=CurrencyChoice.choices,
        verbose_name="валюта",
        default=CurrencyChoice.RUB,
    )
    recip_details = models.TextField(verbose_name="реквизиты получателя")
    status = models.IntegerField(
        choices=StatusChoice.choices,
        verbose_name="статус заявки",
        default=StatusChoice.OPENED,
    )
    description = models.TextField(verbose_name="описание или комментарий", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата обновления")

    class Meta:
        verbose_name = "Заявка на выплату"
        verbose_name_plural = "Заявки на выплату"
        ordering = [
            "id",
        ]

    def __str__(self):
        return f"Заявка {self.id}: сумма {self.payment}"
